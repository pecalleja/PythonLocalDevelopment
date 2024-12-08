# fmt: off
"""
Rotating a Singly Linked List to the Right

You are given a singly linked list and an integer k. Your task is to write a
Python function, rotate_right(linked_list, k), which rotates the linked list
to the right by k places. Note that k might be 0 or greater than the length
of the linked list.

Your function should take the last k nodes from the end of the list and move
them to the start of the list, maintaining their original order. After the
rotation, return the head of the resulting linked list.

For instance, if the linked list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, after the
rotation, it should become 4 -> 5 -> 1 -> 2 -> 3.

The expected time complexity for your solution is O(n).
"""
from src.common import ListNode
# fmt: on


def solution(head: ListNode, k: int) -> ListNode:
    # Edge case: empty list or k is 0
    if not head or k == 0:
        return head

    # Step 1: Calculate the length of the linked list
    length = 1  # At least one node is present
    tail = head  # Start from the head

    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Update k to handle cases where k >= length
    k = k % length
    if k == 0:
        return head  # No rotation needed

    # Step 3: Find the new tail (n-k-1)th node
    new_tail_position = length - k - 1
    new_tail = head

    for _ in range(new_tail_position):
        new_tail = new_tail.next

    # Step 4: Update pointers to rotate
    new_head = new_tail.next  # New head is the next node after new tail
    new_tail.next = None  # Break the list here
    tail.next = head  # Connect original tail to the original head

    return new_head
