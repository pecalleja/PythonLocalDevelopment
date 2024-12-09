"""
Detecting a Cycle in a Linked List

You are given a linked list, and you are required to detect if a cycle exists
in the linked list. A linked list is said to contain a cycle if a node's next
pointer points back to one of the previous nodes in the list. Given the head
of the linked list head, return True if the linked list contains a cycle and
False otherwise.

You need to solve this using O(1) of additional memory.
"""


def solution(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
