--!strict
-- String helpers that do not modify their input.

local StringUtils = {}

function StringUtils.trim(value: string): string
    return (string.gsub(value, "^%s*(.-)%s*$", "%1"))
end

-- Splits on a literal, non-empty separator. Empty fields are preserved,
-- including a trailing empty field.
function StringUtils.split(value: string, separator: string): {string}
    assert(separator ~= "", "separator must not be empty")

    local parts = {}
    local startIndex = 1

    while true do
        local foundStart, foundEnd = string.find(value, separator, startIndex, true)
        if foundStart == nil then
            table.insert(parts, string.sub(value, startIndex))
            break
        end

        table.insert(parts, string.sub(value, startIndex, foundStart - 1))
        startIndex = foundEnd + 1
    end

    return parts
end

return StringUtils
