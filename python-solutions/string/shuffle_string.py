#!/usr/bin/env python

from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    sl = list(s)
    idx_to_str = {}
    for i in range(len(sl)):
        idx_to_str[indices[i]] = sl[i]
    indices.sort()
    result = ''
    for idx in indices:
        result += idx_to_str[idx]
    return result


def main():
    s1 = 'aaiougrt'
    indices1 = [4, 0, 2, 6, 7, 3, 1, 5]
    r1 = restoreString(s1, indices1)
    print(r1)


if __name__ == '__main__':
    main()
