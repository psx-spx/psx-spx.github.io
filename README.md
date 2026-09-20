# psx-spx

PlayStation 1 hardware specifications, published at
<https://psx-spx.consoledev.net/>.

The text started as Martin Korth's
[psx-spx](https://problemkaputt.de/psx-spx.htm), converted to markdown once by the awk
script in [conversion](conversion/). Everything since then was written here: register
behaviour checked against real consoles, timings, disc formats, motherboard revisions,
and a lot of what the original document left open. Forty-odd people have had a hand in
it.

## Reading it

The rendered site is the thing to read; it also builds as a single PDF, linked from the
site. Bit-layout diagrams are drawn above each register table at build time by
[tools/bitfields](tools/bitfields/), straight from the table, so the two cannot drift
apart.

## Changing it

Every page has an edit link that takes you to it on GitHub. For anything larger, clone
and run it locally:

```sh
pip install -r requirements.txt
mkdocs serve
```

A push to `master` deploys the site, so send a pull request if you are not sure about a
change. Say how you know: a test program, a capture, a register dump. If you suspect a
page is wrong but cannot show it yet, open an
[issue](https://github.com/psx-spx/psx-spx.github.io/issues) and say so there.

## Elsewhere

[ps1dev/standards](https://github.com/ps1dev/standards) has the file formats homebrew
tools agree on. [pcsx-redux](https://github.com/grumpycoders/pcsx-redux) is an emulator
and toolchain that much of the testing behind these pages runs on. The
[PSX.Dev Discord server](https://discord.gg/QByKPpH) is where most of it gets hashed
out.

Credits for the original documentation are on the
[About & Credits](https://psx-spx.consoledev.net/aboutcredits/) page.
