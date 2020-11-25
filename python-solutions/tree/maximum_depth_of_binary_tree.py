#!/usr/bin/env python

from common.binary_tree import TreeNode, construct_binary_tree

# Solution to https://leetcode.com/problems/maximum-depth-of-binary-tree/

def max_depth(root: TreeNode) -> int:
    if root:
        return 1 + max(max_depth(root.left),  max_depth(root.right))
    else:
        return 0

def max_depth_recursion(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        left_height = max_depth_recursion(root.left)
        right_height = max_depth_recursion(root.right)
        return 1 + left_height if left_height >= right_height else 1 + right_height


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    height = 1
    max_height = 0
    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        seen.add(node)
        if node.left and node.left not in seen:
            stack.append(node.left)
        if node.right and node.right not in seen:
            stack.append(node.right)
        height += 1

        if height > max_height:
            max_height = height

    return max_height


def main():
    small_input = [3, 9, 20, None, None, 15, 7]
    root = construct_binary_tree(small_input, 0)
    maximum_depth = max_depth(root)
    print(maximum_depth)

    result = max_depth_recursion(root)
    print(result)


if __name__ == '__main__':
    main()
