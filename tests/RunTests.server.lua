--!strict
-- Copy this Script into a test location in Roblox Studio and update module paths.
-- This lightweight runner uses built-in assertions; no third-party framework is required.

local root = script.Parent.Parent
local TableUtils = require(root.src.TableUtils)
local StringUtils = require(root.src.StringUtils)
local NumberUtils = require(root.src.NumberUtils)

local passed = 0

local function test(name: string, callback: () -> ())
    local success, message = pcall(callback)
    if not success then
        error("FAILED: " .. name .. " - " .. tostring(message))
    end
    passed += 1
    print("PASS: " .. name)
end

test("deepCopy separates nested tables", function()
    local original = { nested = { value = 10 } }
    local copied = TableUtils.deepCopy(original)
    copied.nested.value = 20
    assert(original.nested.value == 10)
end)

test("deepCopy preserves cycles", function()
    local original = {}
    original.self = original
    local copied = TableUtils.deepCopy(original)
    assert(copied ~= original)
    assert(copied.self == copied)
end)

test("shallowEquals checks key/value equality", function()
    assert(TableUtils.shallowEquals({a = 1, b = 2}, {a = 1, b = 2}))
    assert(not TableUtils.shallowEquals({a = 1, b = 2}, {a = 1}))
end)

test("trim removes surrounding whitespace", function()
    assert(StringUtils.trim("  hello  ") == "hello")
end)

test("split preserves empty fields", function()
    local parts = StringUtils.split("a,,b,", ",")
    assert(#parts == 4)
    assert(parts[1] == "a" and parts[2] == "" and parts[3] == "b" and parts[4] == "")
end)

test("clamp bounds values", function()
    assert(NumberUtils.clamp(12, 0, 10) == 10)
    assert(NumberUtils.clamp(-2, 0, 10) == 0)
    assert(NumberUtils.clamp(5, 0, 10) == 5)
end)

test("map converts between ranges", function()
    assert(NumberUtils.map(5, 0, 10, 0, 100) == 50)
end)

print(string.format("All %d tests passed.", passed))
