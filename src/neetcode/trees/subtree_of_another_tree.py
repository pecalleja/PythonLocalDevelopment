from .same_tree import Solution
from src.common import TreeNode


class Solution(Solution):
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(
            root.right, subRoot
        )
