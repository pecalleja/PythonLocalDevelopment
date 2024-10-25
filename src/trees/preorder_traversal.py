from typing import List
from typing import Optional

from src.trees import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            inorder(node.left)  # Traverse left subtree
            inorder(node.right)  # Traverse right subtree

        inorder(root)
        return result
