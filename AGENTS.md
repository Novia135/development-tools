# Instructions for coding agents

These instructions apply to the entire repository.

## Project purpose

Maintain a small, readable collection of reusable Roblox Luau utilities. The project is early-stage. Do not describe it as widely adopted, production-proven, audited, or benchmarked unless verifiable evidence is added.

## Before changing code

1. Read this file and the repository README.
2. Inspect the relevant module, tests, and examples before editing.
3. Preserve existing public API behavior unless the task explicitly requests a breaking change.
4. Check Roblox Luau semantics rather than assuming stock Lua behavior.

## Implementation standards

- Write clear, idiomatic Luau.
- Keep modules focused and dependency-free unless a dependency is justified and documented.
- Validate public inputs where doing so prevents confusing failures.
- Use descriptive names and document non-obvious behavior.
- Avoid unnecessary abstractions, global state, networking, DataStore access, or side effects in utility modules.
- Never include credentials, tokens, private player information, or proprietary game code.
- Do not add telemetry, hidden network calls, obfuscated code, or executable installation steps.

## Tests and verification

- Add or update tests for every behavior change.
- Include normal cases and relevant edge cases.
- Do not claim tests passed unless they were actually run in a Roblox Luau runtime.
- If Studio execution is unavailable, state that tests were not run and provide exact manual verification steps.
- Keep examples aligned with the actual exported API.

## Documentation and releases

- Update README or module documentation when public behavior changes.
- Record user-visible changes in CHANGELOG.md.
- Mark breaking changes clearly.
- Do not invent downloads, dependent repositories, usage statistics, contributors, benchmarks, endorsements, or compatibility guarantees.

## Scope

Do not modify Roblox experiences or Studio projects as part of repository-only tasks. Work only on files in this GitHub repository unless the user explicitly requests otherwise.
