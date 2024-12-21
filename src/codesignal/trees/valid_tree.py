"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Binary Search Tree Verification

Your task is to implement a function is_binary_search_tree(root) that takes
the root of a binary tree as input and returns a Boolean, indicating whether
the input tree is a binary search tree. In a binary search tree, for each
node, its value is greater than or equal to the values of all nodes in its
left subtree and less than or equal to the values of all nodes in its right
subtree. It's guaranteed that all node values are distinct.

The expected time complexity of your solution is O(n), where n is the number
of nodes in the binary tree. Make sure to implement the solution that goes
through every tree's node only once.
"""

from src.common import TreeNode


def solution(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return validate(node.left, min_val, node.val) and validate(
            node.right, node.val, max_val
        )

    # Start with the full range of valid values
    return validate(root, float("-inf"), float("inf"))
