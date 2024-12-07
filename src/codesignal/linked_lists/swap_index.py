# fmt: off
"""
Swapping Nodes in a Singly Linked List at Given Indices

You are given a singly linked list and two indices, start and end (both
indices are 0-based). Write a Python function swap_linked_list_nodes(head:
ListNode, start: int, end: int) -> ListNode that swaps the nodes of the
linked list at these two provided indices. The function should return the head
node of the modified linked list. When swapping, you should only change the
next property of a node, not the actual node values. It is guaranteed that
start <= end.

For example, consider the linked list 1 -> 2 -> 3 -> 4 -> 5 and you are given
start = 1 and end = 3. The resulting linked list after swapping nodes at
indices 1 and 3 would be:

1 -> 4 -> 3 -> 2 -> 5

The expected time complexity of your solution should be
O(n), where n is the length of the linked list.
"""
from src.common import ListNode
# fmt: on


def solution(head, start, end):
    if start == end:  # No swap needed if the indices are the same
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev_start, prev_end = dummy, dummy
    node_start, node_end = head, head

    # Traverse to the start and end indices
    for _ in range(start):
        prev_start = node_start
        node_start = node_start.next
    for _ in range(end):
        prev_end = node_end
        node_end = node_end.next

    # Handle adjacency case
    if node_start.next == node_end:
        prev_start.next = node_end
        node_start.next = node_end.next
        node_end.next = node_start
    else:
        # Swap the nodes
        prev_start.next = node_end
        prev_end.next = node_start
        node_start.next, node_end.next = node_end.next, node_start.next

    return dummy.next
