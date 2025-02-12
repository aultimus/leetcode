# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            chars = ""
            for j in range(i, len(s)):
                char = s[j]
                if char in chars:
                    break
                chars += char
                length = len(chars)
                if length > longest:
                    longest = length
                    print(chars, length)
        return longest
        # optimisation - return early when size of substring found so far
        # is greater than any that we can possibly find (near end of string)

        # also a more efficient solution would be to work backwards rather than
        # forwards, that is test the longest string first.
        #
        # Once you have found a long string you can stop checking any shorter
        # strings


test_data = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.mark.parametrize("input,expected", test_data)
def test_all(input, expected):
    assert expected == Solution().lengthOfLongestSubstring(input)
