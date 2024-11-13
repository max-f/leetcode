#!/usr/bin/env python


def remove_element(nums: list[int]) -> int:
    i = 0
    removed = 0
    last_seen = None
    starting_length = len(nums)

    while i < starting_length - removed:
        x = nums[i]
        if x == last_seen:
            del nums[i]
            removed += 1
            continue
        last_seen = x
        i += 1
    return len(nums)


def main():
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_element(a)
    print(a)
    print(result)


if __name__ == "__main__":
    main()
