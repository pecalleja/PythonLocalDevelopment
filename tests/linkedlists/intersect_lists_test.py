import pytest

from src.linkedlists.intersect_lists import Solution


def create_intersection(headA, headB, intersect_val):
    if not headA or not headB:
        return

    intersect_node = None
    currentA, currentB = headA, headB

    while currentA:
        if currentA.val == intersect_val:
            intersect_node = currentA
            break
        currentA = currentA.next

    if intersect_node:
        while currentB.next:
            currentB = currentB.next
        currentB.next = intersect_node


@pytest.mark.parametrize(
    "listA, listB, intersect_val, expected",
    [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 8, 8),
        ([1, 9, 1, 2, 4], [3, 2, 4], 2, 2),
        ([2, 6, 4], [1, 5], None, None),
        ([1, 2, 3], [4, 5, 6], None, None),
        ([1, 2, 3], [3, 4, 5], 3, 3),
    ],
)
def test_getIntersectionNode(
    build_linked_list, listA, listB, intersect_val, expected
):
    sol = Solution()
    headA = build_linked_list(listA)
    headB = build_linked_list(listB)
    if intersect_val is not None:
        create_intersection(headA, headB, intersect_val)
    result = sol.getIntersectionNode(headA, headB)
    assert (result.val if result else None) == expected
