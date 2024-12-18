"""
Reversing a Binary Tree in Python

Given a binary tree, write a function in Python to reverse the given binary
tree. This means that for every node in the binary tree, you have to swap its
left and right child nodes.
"""

from typing import Optional

from src.common import TreeNode


def solution(root: TreeNode) -> Optional[TreeNode]:
    def preorder(node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return root
