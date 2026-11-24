# Project status

Last updated: 2026-11-24

This repository is in early development. It is a general-purpose developer-tools project with a small Python CLI and an optional Roblox Luau utilities folder.

## Implemented

- Python module entry point: python -m devtools.
- Read-only TODO/FIXME/XXX text scanner.
- Read-only text file and line inventory grouped by extension.
- Human-readable and JSON output.
- Default exclusions for common generated, dependency, and version-control directories.
- Python unit tests using temporary directories and the standard library.
- Existing Luau table, string, and number helpers and a Studio-oriented test script.

## Validation status

The Python unit tests are included but have not been executed in this GitHub workflow. No CI result is claimed. The Luau test script has not been run in Roblox Studio. No independent security audit, broad platform matrix, external adoption, download count, dependent-project count, or versioned release is claimed.

## Known limitations

- Scanning is text-based and UTF-8-only; undecodable files are skipped.
- Marker matching is simple substring matching, not syntax-aware.
- Statistics are approximate text line counts, not language-specific metrics.
- Large repositories can take time to scan.

## Next steps

Prioritize concrete user needs. Candidate improvements include configurable ignore rules, Git-aware changed-file inspection, CI on supported Python versions, and additional tests. These are proposals, not completed features.
