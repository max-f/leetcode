#!/usr/bin/env python

from typing import List

"""
Code for https://leetcode.com/problems/subrectangle-queries
"""

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# [[1, 2, 3], [4, 5, 6]]
#      c1 c2 c3
# row1  1  2  3
# row2  4  5  6


def main():
    s = SubrectangleQueries([[1, 2, 3], [4, 5, 6]])
    print(s.getValue(1, 2))


if __name__ == "__main__":
    main()