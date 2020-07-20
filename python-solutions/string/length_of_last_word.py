#!/usr/bin/env python

import re

def length_of_last_word(s: str) -> int:
    pattern = re.compile("(\w*$)")
    m = re.search(pattern, s.rstrip())
    return len(m.group(1))


def main():
    s = "Hello World "
    result = length_of_last_word(s)
    print(result)


if __name__ == '__main__':
    main()
