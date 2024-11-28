from src.neetcode.trees import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(
                left.right, right.left
            )

        return is_mirror(root.left, root.right)
