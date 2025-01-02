from src.common import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, left_max + right_max + node.val)
            return max(left_max, right_max) + node.val

        dfs(root)
        return self.max_sum
