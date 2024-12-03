from src.neetcode.trees import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Update the diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)
            # Return the height of the tree
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter
