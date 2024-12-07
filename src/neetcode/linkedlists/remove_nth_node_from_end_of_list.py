from src.common import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move `first` pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move `first` to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next
