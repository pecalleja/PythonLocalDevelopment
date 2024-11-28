from src.neetcode.stacks.min_stack import MinStack


def test_min_stack():
    # Initialize MinStack
    min_stack = MinStack()

    # Test push operation
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    # Test getMin operation
    assert min_stack.getMin() == -3  # The minimum is -3

    # Test pop operation
    min_stack.pop()  # Pop the top, which is -3

    # Test top operation
    assert min_stack.top() == 0  # The current top is 0

    # Test getMin operation again
    assert min_stack.getMin() == -2  # The minimum is now -2


def test_min_stack_edge_case():
    min_stack = MinStack()

    # Test single push, pop and getMin operations
    min_stack.push(1)
    assert min_stack.getMin() == 1  # The only element is the minimum

    min_stack.pop()  # Pop the only element

    # After popping the only element, pushing more elements
    min_stack.push(-1)
    min_stack.push(2)
    min_stack.push(0)

    assert min_stack.getMin() == -1  # The minimum is -1
    min_stack.pop()  # Pop 0
    assert min_stack.getMin() == -1  # The minimum is still -1
