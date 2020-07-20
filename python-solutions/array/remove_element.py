#!/usr/bin/env python

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i = 0
    removed = 0
    starting_length = len(nums)

    while i < starting_length - removed:
        x = nums[i]
        if x == val:
            del nums[i]
            removed += 1
            continue
        i += 1
    return len(nums)


def main():
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    result = remove_element(a, 2)
    print(a)
    print(result)


if __name__ == "__main__":
    main()
