from typing import Optional

from src.common import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        # Traverse the tree
        while root:
            if p.val < root.val and q.val < root.val:
                # Both nodes are in the left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # Both nodes are in the right subtree
                root = root.right
            else:
                # We found the split point; this is the LCA
                return root
        return None
