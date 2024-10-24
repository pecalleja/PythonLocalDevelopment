from src.linkedlists import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        return False
