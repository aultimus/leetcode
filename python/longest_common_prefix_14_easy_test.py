# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    shortest_word = min(filter(None, strs), key=len)
    prefix = ""
    for i in range(0, len(shortest_word)):
        prefix = strs[0][: i + 1]
        for word in strs:
            if not word.startswith(prefix):
                return prefix[:-1]
    return prefix


def test_simple():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_no_prefix():
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_short():
    assert longest_common_prefix(["at", "a", "ate"]) == "a"


def test_med():
    assert longest_common_prefix(["flap", "flat", "flatter", "flat"]) == "fla"


def test_long():
    assert longest_common_prefix(["helper", "helpers", "help"]) == "help"


def test_same():
    assert longest_common_prefix(["fate", "fate", "fate", "fate"]) == "fate"
