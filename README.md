# Roblox Development Tools

A small, openly developed collection of reusable Luau utilities for Roblox experiences.

> **Project status:** Early development. APIs may change, and modules should be reviewed and tested in your own experience before production use. This repository does not claim production adoption or independent security review.

## Goals

- Provide focused utilities that are easy to read and adapt.
- Keep modules dependency-free and compatible with Roblox Luau.
- Document behavior, edge cases, and examples.
- Prefer explicit APIs over hidden global state.

## Contents

| Path | Description |
| --- | --- |
| `src/TableUtils.lua` | Copying and table inspection helpers |
| `src/StringUtils.lua` | String trimming and splitting helpers |
| `src/NumberUtils.lua` | Numeric validation and mapping helpers |
| `tests/RunTests.server.lua` | Simple in-experience assertion-based test runner |
| `examples/Usage.server.lua` | Example usage from a server Script |

## Installation

1. Review the source files in `src/`.
2. Copy the modules you need into `ServerScriptService`, `ReplicatedStorage`, or another suitable location.
3. Require the ModuleScript from a Script or LocalScript as appropriate.
4. Review each module's comments and test it in Studio before relying on it.

These files are plain Luau source. They are not a Roblox model or plugin package.

## Quick example

```lua
local NumberUtils = require(path.to.NumberUtils)
local TableUtils = require(path.to.TableUtils)

local chance = NumberUtils.clamp(1.4, 0, 1)
local settings = TableUtils.deepCopy({
    audio = { volume = 0.7 },
})

print(chance) -- 1
print(settings.audio.volume) -- 0.7
```

Replace `path.to` with the actual ModuleScript location in your experience.

## Testing

Place `tests/RunTests.server.lua` in a server Script and update its `require` paths to match where you placed the modules. Run the experience in Studio and check the Output window. The test runner uses built-in assertions and has no external test-framework dependency.

## Compatibility

The modules target Roblox Luau and use standard Luau/Roblox runtime behavior. They are not intended to run unchanged in stock Lua interpreters. Check the source for any runtime-specific assumptions.

## Contributing

Bug reports, documentation improvements, and focused utility proposals are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Security

Do not put secrets, API keys, private game code, player data, or credentials in this repository. See [SECURITY.md](SECURITY.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
