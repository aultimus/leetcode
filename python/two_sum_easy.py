# https://leetcode.com/problems/two-sum/description/

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                return [i, j]
    return []


# TODO: parameterize tests
def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    assert [0, 1] == twoSum(nums, target)


def test_2():
    nums = [3, 2, 4]
    target = 6
    assert [1, 2] == twoSum(nums, target)


def test_3():
    nums = [3, 3]
    target = 6
    assert [0, 1] == twoSum(nums, target)
