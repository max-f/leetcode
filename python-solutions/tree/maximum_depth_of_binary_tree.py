#!/usr/bin/env python

from common.binary_tree import TreeNode, construct_binary_tree

# Solution to https://leetcode.com/problems/maximum-depth-of-binary-tree/

def max_depth(root: TreeNode) -> int:
    if root:
        return 1 + max(max_depth(root.left),  max_depth(root.right))
    else:
        return 0


def main():
    small_input = [3, 9, 20, None, None, 15, 7]
    root = construct_binary_tree(small_input, 0)
    maximum_depth = max_depth(root)
    print(maximum_depth)


if __name__ == '__main__':
    main()
