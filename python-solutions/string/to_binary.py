#!/usr/bin/env python

"""
Convert a decimal number to binary, using strings
"""


def to_binary(num: int) -> int:
    new_number = ""
    while num:
        new_number = f"{num % 2}{new_number}"
        num //= 2
    return int(new_number)


def main():
    result = to_binary(13)
    print(result)


if __name__ == "__main__":
    main()
