from typing import List
from typing import Optional

from src.common import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            result.append(node.val)  # Visit root
            inorder(node.right)  # Traverse right subtree

        inorder(root)
        return result
