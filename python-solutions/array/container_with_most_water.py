#!/usr/bin/env python

from typing import List
from utils.my_utils import timeit, get_input


@timeit
def max_area(height: List[int]) -> int:
    # - Currently around n² runtime, omitting calculating stuff twice
    # - Area: A = w*l
    maximum = -1

    for x1, y1 in enumerate(height):
        for x2, y2 in enumerate(height[x1:]):
            max_height = min(y1, y2)
            width = x2
            area = max_height * width
            if area > maximum:
                maximum = area
    return maximum


@timeit
def max_area2(height: List[int]) -> int:
    # Idea:
    # Moving pointers to both borders
    # Write methods to search next bigger height from the left and from the right
    # Move the shorter pointer of both everytime
    # Stop if pointers overlap
    if len(height) <= 1:
        return 0

    maximum = -1
    i = 0
    j = len(height) - 1
    while i < j and i < len(height) and j > 0:
        max_height = min(height[i], height[j])
        width = j - i
        area = max_height * width
        if area > maximum:
            maximum = area

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maximum


def main():
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # heights = [0, 0, 8, 8, 1, 5]
    # input_file = get_input("/home/keks/long_input_container_list")
    # input_trimmed = input_file[1:-1].split(",")
    # heights = [int(x) for x in input_trimmed]
    # heights = [0]
    maximum = max_area(heights)
    print(f"First one: {maximum}")
    maximum2 = max_area2(heights)
    print(f"Second one: {maximum2}")


if __name__ == "__main__":
    main()
