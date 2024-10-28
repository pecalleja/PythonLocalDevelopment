from src.linkedlists import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode:  # noqa
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA
