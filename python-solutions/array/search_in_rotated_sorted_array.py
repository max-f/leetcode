#!/usr/bin/env python

from typing import List, Tuple
from bisect import bisect_left

"""
Code for https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


def search(nums: List[int], target: int) -> int:
    pivot_idx = find_pivot(nums, 0, len(nums) - 1)
    if pivot_idx == -1:
        return binary_search(nums, target, 0, len(nums) - 1)

    if nums[pivot_idx] == target:
        return pivot_idx
    if nums[0] <= target:
        return binary_search(nums, target, 0, pivot_idx - 1)
    return binary_search(nums, target, pivot_idx + 1, len(nums) - 1)


def binary_search(a: List[int], x: int, lo: int, hi: int) -> int:
    idx = bisect_left(a, x, lo, hi)
    return idx if idx != len(a) and a[idx] == x else -1


def find_pivot(nums: List[int], lo: int, hi: int) -> int:
    """
    Find index of pivot element if nums is indeed rotated, else return -1
    """

    # Base cases to prevent endless recursion
    if lo > hi:
        return -1
    if lo == hi:
        return lo

    mid = (lo + hi) // 2
    if mid < hi and nums[mid] > nums[mid + 1]:
        return mid
    if mid > lo and nums[mid] < nums[mid - 1]:
        return mid - 1
    if nums[lo] >= nums[mid]:
        return find_pivot(nums, lo, mid - 1)
    return find_pivot(nums, mid + 1, hi)


def main():
    xs = [3, 1]
    xs2 = [4, 5, 6, 7, 0, 1, 2]
    xs3 = [6, 7, 1, 2, 3, 4, 5]
    result = search(xs, 3)
    result2 = search(xs2, 0)
    result3 = search(xs3, 6)
    print(result)
    print(result2)
    print(result3)


if __name__ == "__main__":
    main()
