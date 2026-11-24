--!strict
-- Small table helpers. These functions do not mutate the input table.

local TableUtils = {}

-- Copies nested tables. Non-table values (including Instances and functions)
-- are retained by reference/value. Cycles and shared table references are preserved.
function TableUtils.deepCopy<T>(source: T): T
    local seen: {[any]: any} = {}

    local function copy(value: any): any
        if type(value) ~= "table" then
            return value
        end

        if seen[value] ~= nil then
            return seen[value]
        end

        local result = {}
        seen[value] = result

        for key, child in pairs(value) do
            result[copy(key)] = copy(child)
        end

        return setmetatable(result, getmetatable(value))
    end

    return copy(source) :: T
end

-- Returns true when every key in expected exists in actual with an equal value.
-- This is a shallow comparison; nested tables are compared by identity.
function TableUtils.shallowEquals(actual: {[any]: any}, expected: {[any]: any}): boolean
    for key, value in pairs(expected) do
        if actual[key] ~= value then
            return false
        end
    end

    for key in pairs(actual) do
        if expected[key] == nil and actual[key] ~= nil then
            return false
        end
    end

    return true
end

return TableUtils
