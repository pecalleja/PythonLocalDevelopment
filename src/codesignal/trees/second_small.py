# fmt: off
"""
Finding the Second-Smallest Node in a Binary Tree

Imagine we are given a binary tree in which each node contains an integer.
Your task is to write a Python function that traverses this binary tree and
returns the second-smallest value among all the tree nodes. If there's no
second-smallest number (for example, if all the values in the tree are the
same, or if there's only one node in the tree), the function should return
None.

You are not allowed to use sort() or any other built-in sorting methods in
your solution. You should use Binary Tree Traversal techniques, which we
have discussed in the lesson.

Expected complexity is O(n), where n is the number of vertices in the binary
tree. The expected additional memory is O(1).
"""
from typing import Optional

from src.common import TreeNode
# fmt: on


def solution(root: TreeNode) -> Optional[TreeNode]:
    if not root or (not root.left and not root.right):
        return None

    first = float("inf")
    second = float("inf")

    def inorder(node: TreeNode) -> Optional[TreeNode]:
        nonlocal first, second
        if not node:
            return

        inorder(node.left)

        if node.val < first:
            second = first
            first = node.val
        elif first < node.val < second:
            second = node.val

        inorder(node.right)

    inorder(root)

    return second if second < float("inf") else None
