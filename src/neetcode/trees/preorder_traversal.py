from typing import List
from typing import Optional

from src.common import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            preorder(node.left)  # Traverse left subtree
            preorder(node.right)  # Traverse right subtree

        preorder(root)
        return result
