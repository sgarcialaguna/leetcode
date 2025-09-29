import pytest

lookup = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def romanToInteger(roman: str) -> int:
    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i : i + 2] in lookup:
            result += lookup[roman[i : i + 2]]
            i += 2
            continue

        result += lookup[roman[i]]
        i += 1

    return result


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_romanToInteger(roman: str, expected: int):
    assert romanToInteger(roman) == expected
