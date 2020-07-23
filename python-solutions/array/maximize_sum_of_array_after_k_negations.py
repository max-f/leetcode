#!/usr/bin/env python

from typing import List
from heapq import heapify, heappush, heappop

"""
Code for https://leetcode.com/contest/weekly-contest-127/problems/maximize-sum-of-array-after-k-negations/
"""


def largest_sum_after_k_negations(A: List[int], k: int) -> int:
    """
    Find k min elements of list with the most/least effect on sum
    Sort list and get k-first elements
    :param A: Array of integers
    :param k: Times to modify any index by negation
    :return: Largest possible sum of integer array
    """
    A.sort()
    k_mins = A[:k]
    invert_indices = []
    for (ix, x) in enumerate(k_mins):
        if x < 0:
            # We want to invert every negative number if possible
            invert_indices.append(ix)
        elif x == 0 or k - len(invert_indices) % 2 == 0:
            # Zero or even remaining shifts can be cancelled out
            remaining_times = k - len(invert_indices)
            invert_indices.extend([ix] * remaining_times)
            break
        else:
            # Remaining shifts are not even, check for 'minimal dmg'
            remaining_times = k - len(invert_indices)
            abs_value_cur = abs(x)
            if ix:
                last_negative = abs(k_mins[ix - 1])
                if last_negative < abs_value_cur:
                    invert_indices.extend([ix - 1] * remaining_times)
                    break
            invert_indices.extend([ix] * remaining_times)
            break

    for ix in invert_indices:
        A[ix] = -A[ix]
    return sum(A)


def largest_sum_after_k_negations_heap(A: List[int], k: int) -> int:
    """
    Use a heap.
    """
    heapify(A)
    for _ in range(k):
        min_x = heappop(A)
        heappush(A, -min_x)
    return sum(A)


def main():
    result = largest_sum_after_k_negations([2, -3, -1, 5, -4], 2)
    print(result)
    result_heap = largest_sum_after_k_negations_heap([2, -3, -1, 5, -4], 2)
    print(result_heap)


if __name__ == "__main__":
    main()
