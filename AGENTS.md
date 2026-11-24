# Instructions for coding agents

This is a small, cross-platform developer-tools project. Read this file and relevant documentation before changing code.

## Project boundaries

- General-purpose Python CLI: devtools/
- Python tests: tests/python/
- Optional Roblox Luau modules: src/
- Luau Studio-oriented test script: tests/RunTests.server.lua
- Do not describe the repository as Roblox-only.
- Do not claim features, test results, compatibility, users, downloads, or adoption that have not been verified.

## Before editing

1. Inspect relevant source, tests, README, and project status.
2. Identify the user problem addressed by the change.
3. Check for existing helpers before adding another.
4. Keep changes focused and explain trade-offs.
5. Never overwrite unrelated user work.

## Implementation standards

- Prefer small functions and standard-library dependencies.
- Preserve cross-platform behavior on Windows, macOS, and Linux.
- Keep inspection commands read-only; never execute files being inspected.
- Do not add telemetry, network calls, destructive operations, or credential access without explicit discussion and approval.
- Handle filesystem errors and undecodable files deliberately.
- Add tests for new behavior and edge cases.
- Document machine-readable output and compatibility assumptions.

## Validation and reporting

- Run relevant tests when an execution environment is available.
- If tests cannot be run, say so; never report them as passing.
- Distinguish implemented behavior from planned work.
- Update documentation and CHANGELOG.md for user-visible changes.
- Never fabricate benchmarks, security audits, users, contributors, downloads, dependent repositories, or release history.

## Security

Never commit secrets, tokens, credentials, private source code, or personal data. Treat scanned files as untrusted input. Follow SECURITY.md for vulnerability reports.
