# Development Tools

A small, cross-platform collection of practical utilities for software development.

> **Status:** Early development. Interfaces may change. The Python CLI is the current cross-platform focus; the existing Luau helpers remain an optional language-specific component.

## Current features

### Python command-line tools

Requires Python 3.10+ and has no third-party runtime dependencies.

```sh
python -m devtools --help
python -m devtools scan .
python -m devtools stats .
python -m unittest discover -s tests/python -v
```

- **scan** finds TODO, FIXME, and XXX markers in UTF-8 text files.
- **stats** counts readable text files and lines grouped by file extension.
- Both commands are read-only, support JSON output, and skip common generated and dependency directories by default.

### Optional Roblox Luau helpers

The src directory contains table, string, and numeric helper modules. They are independent of the Python CLI and require a Luau-compatible runtime for validation.

## Install and use

```sh
git clone https://github.com/Novia135/development-tools.git
cd development-tools
python -m devtools --help
```

No installation is required when running from the repository root. A packaged command may be added after the interface stabilizes.

## Commands

```sh
python -m devtools scan PATH [--include-hidden] [--json]
python -m devtools stats PATH [--include-hidden] [--json]
```

The scanner reports relative file paths, line numbers, marker types, and matching lines. Statistics are approximate text-based counts, not language-aware complexity metrics. Binary or unreadable files are skipped.

## Layout

- devtools/ — cross-platform Python CLI
- tests/python/ — Python unit tests
- src/ — optional Roblox Luau modules
- tests/RunTests.server.lua — Studio-oriented Luau test script
- examples/ — usage examples
- docs/ — architecture and project status

## Design and privacy

The Python CLI runs locally. It does not upload source code, collect telemetry, make network requests, or execute files it scans. Avoid scanning large generated directories or directories containing secrets if output will be shared.

See CONTRIBUTING.md and SECURITY.md. The project is MIT licensed; see LICENSE.

## Project status

See docs/PROJECT_STATUS.md for implemented features, known limitations, and proposed next steps. No external adoption, download counts, dependent-project counts, security audit, or versioned release is claimed.
