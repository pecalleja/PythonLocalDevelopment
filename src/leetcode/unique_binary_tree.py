"""
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's
(binary search trees), which has exactly n nodes of unique values from 1 to n.
 Return the answer in any order.

 Example:

   1      1       2       3       3
   \       \     / \     /       /
    3       2   1   3   2       1
   /         \         /        \
  2           3       1          2

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
"""  # noqa

from functools import cache
from typing import List, Optional

from src.common import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(left, right):
            return (
                [None]
                if left > right
                else [
                    TreeNode(val, left_tree, right_tree)
                    for val in range(left, right + 1)
                    for left_tree in generate_trees(left, val - 1)
                    for right_tree in generate_trees(val + 1, right)
                ]
            )

        return generate_trees(1, n)
