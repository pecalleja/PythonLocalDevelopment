from typing import Optional

from src.common import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return True, 0
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return balanced, 1 + max(left[1], right[1])

        return dfs(root)[0]
