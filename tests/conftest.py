from collections import deque

import pytest

from src.linkedlists import ListNode
from src.trees import TreeNode


@pytest.fixture
def build_tree_from_list():
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
def build_linked_list():
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
def linked_list_to_list():
    def wrapper(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    return wrapper
