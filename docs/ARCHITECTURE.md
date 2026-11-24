# Architecture

## Scope

Development Tools is a collection of small utilities, not a framework. It currently contains two independent areas:

- devtools/: a cross-platform Python command-line package using the standard library.
- src/: optional Roblox Luau modules retained from the project's initial implementation.

The Python package does not import Roblox APIs. The Luau modules do not depend on Python.

## Python CLI

The module entry point delegates to the CLI, which validates the target directory and dispatches to functions in project.py.

The project module walks directories in stable order, skips common generated and dependency directories, reads UTF-8 text only, and treats undecodable or unreadable files as skipped. It never writes to scanned paths or makes network requests.

## Output and compatibility

Human-readable output is intended for terminals. JSON output supports scripts. Scan paths are relative to the selected root. The supported Python target is 3.10+.

## Design constraints

- Prefer the standard library unless a concrete need justifies a dependency.
- Keep inspection commands read-only.
- Never execute code found in scanned projects.
- Do not imply language-aware parsing: current counts and marker matches are text-based.
- Add tests for filesystem edge cases and use temporary test fixtures.
