from src.linkedlists import ListNode


class Node(ListNode):
    def __init__(self, x: int, n: "Node" = None, random: "Node" = None):
        super().__init__(x, n)
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        # Step 1: Copy nodes and insert them into the original list
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the copied list from the original list
        original = head
        copy = head.next
        copy_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head
