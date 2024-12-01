from collections import deque

import pytest

from src.neetcode.linkedlists import ListNode
from src.neetcode.trees import TreeNode


@pytest.fixture
def tree_to_list():
    def wrapper(root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    return wrapper


@pytest.fixture
def list_to_tree():
    def wrapper(values):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            current = queue.popleft()

            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return root

    return wrapper


@pytest.fixture
def list_to_linkedlist():
    def wrapper(nums, pos=None):
        if not nums:
            return None
        nodes = [ListNode(v) for v in nums]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos is not None:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    return wrapper


@pytest.fixture
def linkedlist_to_list():
    def wrapper(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    return wrapper
