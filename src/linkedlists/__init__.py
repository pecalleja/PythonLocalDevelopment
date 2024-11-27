class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __lt__(self, other):
        # This ensures that ListNode can be compared in the heap
        return self.val < other.val
