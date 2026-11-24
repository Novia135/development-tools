--!strict
-- Numeric helpers with explicit input validation.

local NumberUtils = {}

local function assertFinite(value: number, parameterName: string)
    assert(value == value and value ~= math.huge and value ~= -math.huge,
        parameterName .. " must be a finite number")
end

function NumberUtils.clamp(value: number, minimum: number, maximum: number): number
    assertFinite(value, "value")
    assertFinite(minimum, "minimum")
    assertFinite(maximum, "maximum")
    assert(minimum <= maximum, "minimum must be less than or equal to maximum")

    return math.max(minimum, math.min(maximum, value))
end

-- Maps a value from one range to another. The input is not clamped.
function NumberUtils.map(
    value: number,
    inputMinimum: number,
    inputMaximum: number,
    outputMinimum: number,
    outputMaximum: number
): number
    assertFinite(value, "value")
    assertFinite(inputMinimum, "inputMinimum")
    assertFinite(inputMaximum, "inputMaximum")
    assertFinite(outputMinimum, "outputMinimum")
    assertFinite(outputMaximum, "outputMaximum")
    assert(inputMinimum ~= inputMaximum, "input range must have non-zero width")

    local alpha = (value - inputMinimum) / (inputMaximum - inputMinimum)
    return outputMinimum + alpha * (outputMaximum - outputMinimum)
end

return NumberUtils
