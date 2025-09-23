# Snow Code — the AI coding assistant

Snow Code is a terminal-native, agentic dev tool that understands your codebase and helps you move faster by handling repetitive tasks, clarifying tricky code, and orchestrating Git workflows via natural language.

> This tool is built on top of **OpenHands** (MIT).

## Install

```bash
pip install snowcode # or pipx
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv tool install snowcode
```

## Quick start

### CLI mode
```bash
uvx --python 3.12 --from snowcode snow
```

or simply just
```bash
snow
```

Run `snow --help` for commands and options.

## Configuration

Snowcode is wired to Snowcell’s endpoints. Typical setup steps:

- **Credentials**: Provide your Snowcell API credentials via environment variables or CLI flags (see `snow --help`).
- **Models**: Select a model/provider supported by your Snowcell account (again, see `snow --help` for the exact flags).

## License & Attribution

- **License:** MIT. See `LICENSE` in this distribution.
- **Attribution:** Portions derived from the **OpenHands** project (MIT). Upstream source: <https://github.com/All-Hands-AI/OpenHands>.

