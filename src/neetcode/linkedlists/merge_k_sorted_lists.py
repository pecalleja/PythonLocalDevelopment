from heapq import heappop
from heapq import heappush

from src.neetcode.linkedlists import ListNode


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        heap = []
        # Push the head node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heappush(heap, node)

        # Dummy head for the result list
        dummy = ListNode(0)
        current = dummy

        while heap:
            # Pop the smallest node from the heap
            smallest = heappop(heap)
            current.next = smallest
            current = current.next
            # If the list of the smallest node has more elements,
            # push the next node to the heap
            if smallest.next:
                heappush(heap, smallest.next)

        return dummy.next
