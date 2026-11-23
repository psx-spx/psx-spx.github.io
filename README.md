# psx-spx (development branch)

PlayStation 1 hardware specifications. This repository has two branches, published as
two versions of one site:

- `stable`, served at <https://psx-spx.consoledev.net/>, is the human-maintained
  document. It is the default branch, and pull requests for it go there.
- `master`, this branch, is served at <https://psx-spx.consoledev.net/dev/>. Most of
  what changed here since April 2026 was written by an AI and has not all been reviewed
  by a human. Every page of that version says so.

The text started as Martin Korth's
[psx-spx](https://problemkaputt.de/psx-spx.htm), converted to markdown once by the awk
script in [conversion](conversion/).

## Building it

```sh
pip install -r requirements.txt
mkdocs serve
```

A push to `master` rebuilds `/dev/` only. Bit-layout diagrams are drawn above each
register table at build time by [tools/bitfields](tools/bitfields/).

## Changing it

To fix the human-maintained document, open a pull request against `stable`. Pull
requests against `master` are not taken. If something here looks wrong, an
[issue](https://github.com/psx-spx/psx-spx.github.io/issues) is welcome; say how you
know.

## Elsewhere

[ps1dev/standards](https://github.com/ps1dev/standards) has the file formats homebrew
tools agree on. [pcsx-redux](https://github.com/grumpycoders/pcsx-redux) is an emulator
and toolchain. The [PSX.Dev Discord server](https://discord.gg/QByKPpH) is where most of
it gets hashed out.

Credits for the original documentation are on the
[About & Credits](https://psx-spx.consoledev.net/aboutcredits/) page.
