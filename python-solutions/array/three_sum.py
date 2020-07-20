#!/usr/bin/env python

import time
from collections import defaultdict
from typing import List

"""
Code for https://leetcode.com/problems/3sum
"""


def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    seen = set()

    nums_to_indices = defaultdict(list)
    removed = 0
    nums_reduced = []
    for (ax, a) in enumerate(nums):
        indices_list = nums_to_indices[a]
        if len(indices_list) == 3:
            removed += 1
            continue
        nums_to_indices[a].append(ax - removed)
        nums_reduced.append(a)

    nums = nums_reduced
    for ax, a in enumerate(nums[:-1]):
        for bx in range(ax + 1, len(nums)):
            b = nums[bx]
            if ax == bx:
                continue
            c = -(a + b)
            if c in nums_to_indices:
                for cx in nums_to_indices[c]:
                    if cx != ax and cx != bx:
                        triple = frozenset({a, b, c})
                        if triple in seen:
                            continue
                        seen.add(triple)
                        result.append([a, b, c])
    return result


def main():
    input_nums = [0, 0, 0, 1, -1, 1, -1, 2, 3, -2]
    start = time.time()
    result = three_sum(input_nums)
    end = time.time()
    print(f"{end - start}s passed")


if __name__ == "__main__":
    main()
