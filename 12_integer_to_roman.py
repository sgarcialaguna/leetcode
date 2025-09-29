import pytest

one_lookup = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    0: "",
}

ten_lookup = {
    1: "X",
    2: "XX",
    3: "XXX",
    4: "XL",
    5: "L",
    6: "LX",
    7: "LXX",
    8: "LXXX",
    9: "XC",
    0: "",
}

hundred_lookup = {
    1: "C",
    2: "CC",
    3: "CCC",
    4: "CD",
    5: "D",
    6: "DC",
    7: "DCC",
    8: "DCCC",
    9: "CM",
    0: "",
}

thousand_lookup = {1: "M", 2: "MM", 3: "MMM", 0: ""}


def integerToRoman(num: int) -> str:
    return (
        thousand_lookup[num % 10000 // 1000]
        + hundred_lookup[num % 1000 // 100]
        + ten_lookup[num % 100 // 10]
        + one_lookup[num % 10]
    )


@pytest.mark.parametrize(
    "expected, num",
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
def test_integerToRoman(expected: str, num: int):
    assert integerToRoman(num) == expected
