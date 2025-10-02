import pytest


def splitLines(words: list[str], maxWidth: int) -> list[str]:
    # Count letters including spaces, when maxWidth is exceeded, create a new line
    lineIndex = 0
    lines: list[str] = []
    for word in words:
        # First word in a line is assumed to always fit
        if len(lines) <= lineIndex:
            lines.append(word)
        else:
            # Check current length + 1 space + the next word. Does it fit?
            if len(lines[lineIndex]) + 1 + len(word) > maxWidth:
                lineIndex += 1
                lines.append(word)
            else:
                lines[lineIndex] += f" {word}"

    return lines


def justifyLine(line: str, maxWidth: int) -> str:
    # How many spaces do we need: maxWidth - currentWidth
    words = line.split(" ")
    spacesNeeded = maxWidth - sum((len(word) for word in words))
    # We already have the correct amount of spaces
    if spacesNeeded == len(words) - 1:
        return line

    # Only one word, just append spaces to the end
    if len(words) == 1:
        return words[0] + " " * spacesNeeded

    # Loop around and distribute spaces, starting at the beginning.
    # Do not append spaces to the last word
    for i in range(spacesNeeded):
        words[i % (len(words) - 1)] += " "

    return "".join(words)


def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    # First, determine where to split
    lines = splitLines(words, maxWidth)
    # Then, center justify all lines except the last
    for i, line in enumerate(lines[: len(lines) - 1]):
        lines[i] = justifyLine(line, maxWidth)

    # Add spaces to the last line
    lines[len(lines) - 1] += " " * (maxWidth - len(lines[len(lines) - 1]))
    return lines


@pytest.mark.parametrize(
    "words, maxWidth, expected",
    [
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            ["This is an", "example of text", "justification."],
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            ["What must be", "acknowledgment", "shall be"],
        ),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            [
                "Science is what we",
                "understand well",
                "enough to explain to",
                "a computer. Art is",
                "everything else we",
                "do",
            ],
        ),
    ],
)
def test_splitLines(words: list[str], maxWidth: int, expected: list[str]):
    assert splitLines(words, maxWidth) == expected


@pytest.mark.parametrize(
    "line, maxWidth, expected",
    [
        ("This is an", 16, "This    is    an"),
        ("example of text", 16, "example  of text"),
    ],
)
def test_justifyLine(line: str, maxWidth: int, expected: str):
    assert justifyLine(line, maxWidth) == expected


@pytest.mark.parametrize(
    "line, maxWidth, expected",
    [
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            ["This    is    an", "example  of text", "justification.  "],
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            ["What   must   be", "acknowledgment  ", "shall be        "],
        ),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
        ),
        (
            [
                "ask",
                "not",
                "what",
                "your",
                "country",
                "can",
                "do",
                "for",
                "you",
                "ask",
                "what",
                "you",
                "can",
                "do",
                "for",
                "your",
                "country",
            ],
            16,
            [
                "ask   not   what",
                "your country can",
                "do  for  you ask",
                "what  you can do",
                "for your country",
            ],
        ),
    ],
)
def test_fullJustify(line: list[str], maxWidth: int, expected: str):
    assert fullJustify(line, maxWidth) == expected
