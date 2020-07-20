#!/usr/bin/env python

from typing import List


def create_target_array(nums: List[int], index: List[int]) -> List[int]:
    result = []
    for i in range(len(index)):
        ix = index[i]
        result.insert(ix, nums[i])
    return result


def main():
    nums = list(range(5))
    indices = [0, 1, 2, 2, 1]
    result = create_target_array(nums, indices)
    print(result)


if __name__ == '__main__':
    main()
