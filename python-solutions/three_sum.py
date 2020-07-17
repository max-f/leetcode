#!/usr/bin/env python

import time
from collections import defaultdict
from typing import DefaultDict, List
from pprint import pprint


def three_sum(nums: List[int]):
    result = []
    seen = set()
    all_two_sums = calculate_all_two_sums(nums)

    for (ax, a) in enumerate(nums):
        if -a not in all_two_sums:
            continue
        complementing_pairs = all_two_sums[-a]
        for pair in complementing_pairs:
            bx = pair[0]
            cx = pair[1]
            b = pair[2]
            c = pair[3]
            if ax == bx or ax == cx:
                continue

            triple = frozenset({a, b, c})
            if triple in seen:
                continue
            seen.add(triple)
            result.append([a, b, c])

    return result


def calculate_all_two_sums(nums) -> DefaultDict[int, list]:
    all_two_sums = defaultdict(list)
    for ax in range(len(nums)):
        for bx in range(ax + 1, len(nums)):
            if not bx:
                continue
            a = nums[ax]
            b = nums[bx]
            two_sum = a + b
            new_tuple = (ax, bx, a, b)
            all_two_sums[two_sum].append(new_tuple)
    return all_two_sums


def get_input():
    filename = "/home/keks/input_long"
    with open(filename, "rt") as file_input:
        return file_input.read()


def main():
    input_raw = get_input()[1:-1]
    input = [int(s) for s in input_raw.split(",")]
    # input = [-1, 0, 1, 2, -1, -4]
    # input = [0, 0]
    start = time.time()
    result = three_sum(input)
    end = time.time()
    print(end - start)
    print(len(result))
    pprint(result)


if __name__ == '__main__':
    main()
