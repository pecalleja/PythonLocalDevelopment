from collections import deque

from src.common import TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == "null":
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root
