#!/usr/bin/env python

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(xs: List[int], idx: int) -> TreeNode:
    # Formel: Kinder von Element i -> 2i+1 und 2(i+1)
    if idx >= len(xs) or not xs[idx]:
        return None

    node = TreeNode(xs[idx])
    node.left = construct_binary_tree(xs, 2 * idx + 1)
    node.right = construct_binary_tree(xs, 2 * (idx + 1))
    return node
