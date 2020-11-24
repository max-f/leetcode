#!/usr/bin/env python

from common.binary_tree import TreeNode, construct_binary_tree
from typing import List


# Solution to https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if not nums:
        return None

    if len(nums) == 1:
        return TreeNode(val=nums[0])

    mid = len(nums) // 2
    left = sortedArrayToBST(nums[:mid])
    right = sortedArrayToBST(nums[mid+1:])
    return TreeNode(val=nums[mid], left=left, right=right)


def main():
    small_input = [-10, -3, 0, 5, 9]
    rootOfBST = sortedArrayToBST(small_input)
    print(rootOfBST.val)


if __name__ == '__main__':
    main()
