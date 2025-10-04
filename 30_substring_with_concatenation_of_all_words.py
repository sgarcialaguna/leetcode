from collections import Counter, defaultdict
import pytest


def findSubstring(s: str, words: list[str]) -> list[int]:
    word_length = len(words[0])
    result = []
    word_count = Counter(words)

    for i in range(word_length):
        left = i
        sub_count = defaultdict(int)
        count = 0

        for j in range(i, len(s) - word_length + 1, word_length):
            sub_word = s[j : j + word_length]

            if sub_word in word_count:
                sub_count[sub_word] += 1
                count += 1

                while sub_count[sub_word] > word_count[sub_word]:
                    sub_count[s[left : left + word_length]] -= 1
                    count -= 1
                    left += word_length

                if count == len(words):
                    result.append(left)
            else:
                sub_count.clear()
                count = 0
                left = j + word_length

    return result


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("a", ["a"], [0]),
        (
            "a" * 1000,
            ["a"] * 500,
            list(range(501)),
        ),
    ],
)
def test_findSubstring(s, words, expected):
    assert findSubstring(s, words) == expected
