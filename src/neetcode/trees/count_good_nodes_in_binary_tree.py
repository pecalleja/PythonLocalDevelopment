from src.common import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if not node:
                return 0

            good = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)

            good += dfs(node.left, max_value)
            good += dfs(node.right, max_value)

            return good

        return dfs(root, root.val)
