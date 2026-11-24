# Contributing

Thank you for considering a contribution.

## Before opening an issue

Search existing issues for duplicates. Describe the real problem, expected behavior, a minimal reproduction, operating system, and relevant runtime versions.

## Development setup

Python 3.10+ is required for the cross-platform CLI. The current Python tools use only the standard library.

Run tests from the repository root:

```sh
python -m unittest discover -s tests/python -v
```

## Pull requests

- Keep changes focused and explain the user need.
- Add tests for bug fixes and new behavior.
- Update README or docs when commands or behavior change.
- Explain any proposed third-party dependency.
- Do not include generated files, secrets, credentials, private project code, or unrelated formatting changes.
- State which checks you ran and include their actual results.

For Luau changes, state the runtime assumptions and whether tests were run in Studio. Do not claim Studio validation if it was not performed.

Prefer maintainability, predictable behavior, and honest documentation over activity metrics or feature count.
