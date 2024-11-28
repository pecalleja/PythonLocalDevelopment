from typing import List
from typing import Optional

from src.neetcode.trees import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)  # Traverse left subtree
            postorder(node.right)  # Traverse right subtree
            result.append(node.val)  # Visit root

        postorder(root)
        return result
