"""MkDocs hook: fill docs/whatschanged.md from the git history of docs/.

One entry per change that landed on the branch (first parent, so a merged pull
request counts once, under its title), grouped by week and then by page.
Pure renames are not changes. A change touching more than WIDE pages is listed
once under "Across the site". Entries whose title is only about typos,
spelling, formatting, whitespace or links are dropped, as are reverts and the
change they revert; the build log lists what was dropped.
"""
import datetime
import json
import os
import re
import subprocess

from mkdocs.utils import log

PAGE = 'whatschanged.md'
MARKER = '<!-- tools/changes -->'
WEEKS = 26
WIDE = 8
REDIRECTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'redirects', 'map.json')

NOUN = re.compile(r'\b(typos?|spelling|formatting|whitespace|blank lines?|broken links?|'
                  r'wording|grammar|punctuation|sentence structure|mkdocs warnings|deformat)\b', re.I)
CONTENT = re.compile(r'\b(document|describe|explain|mention|note|clean up|information)\b',
                     re.I)


def cosmetic(title):
    """True when every clause of the title is about typos, formatting or links."""
    t = re.sub(r'\s*\(#\d+\)$', '', title).strip()
    m = re.match(r'^([^:]{1,40}):\s*(.+)$', t)
    if m and not NOUN.search(m.group(1)):
        t = m.group(2)              # drop an "area: " prefix
    t = re.sub(r'^\[[^\]]*\]\s*', '', t)
    clauses = [c for c in re.split(r',|;|\s+and\s+|\s+/\s+', t) if c.strip()]
    return bool(clauses) and all(NOUN.search(c) and not CONTENT.search(c) for c in clauses)


def git(root, *args):
    return subprocess.run(['git', '-C', root] + list(args), check=True,
                          capture_output=True, text=True).stdout


def nav_titles(nav, out=None):
    out = {} if out is None else out
    for item in nav or []:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    out[value] = title
                else:
                    nav_titles(value, out)
    return out


def title_of(docs, titles, path):
    """Title as the site shows it: the nav's, else the first heading. None if gone."""
    if not os.path.exists(os.path.join(docs, path)):
        return None
    if path in titles:
        return titles[path]
    with open(os.path.join(docs, path), encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                return line.lstrip('#').strip()
    return path


def redirected(docs, path):
    """A page removed by the restructure, mapped to where tools/redirects sends it."""
    if os.path.exists(os.path.join(docs, path)):
        return path
    try:
        with open(REDIRECTS, encoding='utf-8') as f:
            target = json.load(f).get(path[:-len('.md')], {}).get('')
    except OSError:
        return path
    if target:
        base = target.split('#')[0].strip('/')
        for cand in (base + '.md', base + '/index.md'):
            if os.path.exists(os.path.join(docs, cand)):
                return cand
    return path


def collect(root, since):
    sep = '\x1e'
    out = git(root, 'log', '--first-parent', '--diff-merges=first-parent', '-M',
              '--name-status', f'--since={since}',
              f'--format={sep}%H%x1f%cI%x1f%P%x1f%s%x1f%b%x1d', '--', 'docs')
    changes = []
    for chunk in out.split(sep)[1:]:
        meta, _, files = chunk.partition('\x1d')
        sha, date, parents, subject, body = meta.split('\x1f', 4)
        title = subject
        m = re.match(r'Merge pull request #(\d+) from ', subject)
        if m:
            first = body.strip().splitlines()[0].strip() if body.strip() else ''
            title = f'{first} (#{m.group(1)})' if first else subject
        reverts = (re.search(r'This reverts commit ([0-9a-f]{7,40})', body)
                   or re.match(r'Revert "(.+)"$', title))
        paths = []
        for line in files.strip().splitlines():
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            st = parts[0]
            if st.startswith('R'):
                paths.append(('R', parts[1], parts[2], st == 'R100'))
            else:
                paths.append((st[0], parts[1], None, False))
        changes.append(dict(sha=sha, date=datetime.datetime.fromisoformat(date),
                            title=title, reverts=reverts.group(1) if reverts else None,
                            paths=paths))
    return changes


def render(root, docs, repo_url, titles):
    if git(root, 'rev-parse', '--is-shallow-repository').strip() == 'true':
        log.warning('changes: shallow clone, the page lists only what the clone has')
    now = datetime.datetime.now(datetime.timezone.utc)
    since = (now - datetime.timedelta(weeks=WEEKS)).strftime('%Y-%m-%dT00:00:00Z')
    changes = collect(root, since)

    # Follow renames forward from newest to oldest, so old paths map to today's page.
    moved = {}
    def current(p):
        seen = set()
        while p in moved and p not in seen:
            seen.add(p)
            p = moved[p]
        return p

    dropped = []
    reverted = {c['reverts'] for c in changes if c['reverts']}
    weeks = {}
    for c in changes:
        pages = set()
        for st, a, b, pure in c['paths']:
            if st == 'R':
                moved[a] = current(b)
                if pure:
                    continue
                a = b
            p = current(a)
            if p.endswith('.md') and p.startswith('docs/') and p != 'docs/' + PAGE:
                pages.add(redirected(docs, p[len('docs/'):]))
        bare = re.sub(r'\s*\(#\d+\)$', '', c['title'])
        if c['reverts'] or bare in reverted or any(c['sha'].startswith(r) for r in reverted):
            dropped.append(('revert', c))
            continue
        if not pages:
            continue
        if cosmetic(c['title']):
            dropped.append(('cosmetic', c))
            continue
        monday = (c['date'].astimezone(datetime.timezone.utc).date()
                  - datetime.timedelta(days=c['date'].astimezone(datetime.timezone.utc).weekday()))
        bucket = weeks.setdefault(monday, {})
        keys = ['*'] if len(pages) > WIDE else sorted(pages)
        for k in keys:
            bucket.setdefault(k, []).append((c, len(pages)))

    for why, c in dropped:
        log.info(f'changes: dropped ({why}) {c["sha"][:7]} {c["title"]}')
    log.info(f'changes: {len(changes)} changes read, {len(dropped)} dropped')

    commit = repo_url.rstrip('/') + '/commit/'
    out = []
    for monday in sorted(weeks, reverse=True):
        out.append(f'## Week of {monday.isoformat()}\n')
        bucket = weeks[monday]
        order = sorted((k for k in bucket if k != '*'),
                       key=lambda k: (title_of(docs, titles, k) or k).lower())
        if '*' in bucket:
            order.insert(0, '*')
        for k in order:
            if k == '*':
                out.append('**Across the site**\n')
            else:
                t = title_of(docs, titles, k)
                out.append(f'**[{t}]({k})**\n' if t else f'**{k}** (page since removed)\n')
            for c, n in bucket[k]:
                d = c['date'].astimezone(datetime.timezone.utc).date().isoformat()
                extra = f' ({n} pages)' if k == '*' else ''
                out.append(f'- {d}: {c["title"]}{extra} '
                           f'([{c["sha"][:7]}]({commit}{c["sha"]}))')
            out.append('')
    if not out:
        out.append('Nothing in this period.')
    return '\n'.join(out) + '\n'


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path.replace(os.sep, '/') != PAGE or MARKER not in markdown:
        return markdown
    docs = config['docs_dir']
    root = os.path.dirname(os.path.abspath(config['config_file_path']))
    try:
        body = render(root, docs, config.get('repo_url') or '', nav_titles(config.get('nav')))
    except (OSError, subprocess.CalledProcessError) as e:
        log.warning(f'changes: git history unavailable ({e})')
        body = 'The change list could not be generated for this build.\n'
    return markdown.replace(MARKER, body)
