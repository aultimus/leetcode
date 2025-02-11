# https://leetcode.com/problems/two-sum/description/

from typing import List

import pytest


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                return [i, j]
    return []


test_data = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize("nums,target,expected", test_data)
def test_all(nums, target, expected):
    assert expected == twoSum(nums, target)
