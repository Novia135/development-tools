--!strict
-- Example server Script. Adjust these require paths to match your ModuleScript layout.

local NumberUtils = require(game.ServerScriptService.DevelopmentTools.NumberUtils)
local StringUtils = require(game.ServerScriptService.DevelopmentTools.StringUtils)
local TableUtils = require(game.ServerScriptService.DevelopmentTools.TableUtils)

local reward = NumberUtils.clamp(125, 0, 100)
local displayName = StringUtils.trim("  Explorer  ")
local defaultSettings = {
    audio = {
        musicVolume = 0.6,
    },
}

local playerSettings = TableUtils.deepCopy(defaultSettings)
playerSettings.audio.musicVolume = 0.8

print("Reward:", reward)
print("Display name:", displayName)
print("Default volume remains:", defaultSettings.audio.musicVolume)
print("Player volume:", playerSettings.audio.musicVolume)
