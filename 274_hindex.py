from typing import List

import pytest


def hindex(citations: List[int]) -> int:
    # For 6,5,3,1,0
    # Are there 6 papers with at least 6 citation? No, there is only one paper with at least 6 citations
    # Are there 5 papers with at least 5 citation? No, there are only two papers with at least 5 citations
    # Are there 3 papers with at least 3 citation? Yes, there are three papers with at least 3 citations

    # For 3,1,1
    # Are there 3 papers with at least 3 citations? No, there is only one paper with at least 3 citations
    # Are there 2 papers with at least 1 citation? Yes, there are two papers with at least 1 citation

    citations.sort(reverse=True)
    n = len(citations)
    hindex = 0
    for i in range(n):
        papers = i + 1
        hindex = max(hindex, min(papers, citations[i]))

    return hindex


@pytest.mark.parametrize(
    "citations, expected", [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([0, 0, 2], 1)]
)
def test_hindex(citations, expected):
    assert hindex(citations) == expected
