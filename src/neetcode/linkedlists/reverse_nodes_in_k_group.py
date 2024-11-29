from src.neetcode.linkedlists import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        # Count the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Process each group
        curr = head
        for i in range(0, length - length % k, k):
            # Start of current group
            start = curr

            # Reverse k nodes
            prev_node = None
            for j in range(k):
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node

            # Connect with the rest of the list
            prev.next = prev_node
            start.next = curr
            prev = start

        return dummy.next
