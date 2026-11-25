from solutions.reverseLinkedList import ListNode, Solution


def make_linked_list(values):
    """Build a linked list and return its head and original node objects."""
    nodes = [ListNode(value) for value in values]

    for current, following in zip(nodes, nodes[1:]):
        current.next = following

    head = nodes[0] if nodes else None
    return head, nodes


def nodes_from(head):
    """Return the nodes in a linked list, in order."""
    nodes = []
    current = head

    while current is not None:
        nodes.append(current)
        current = current.next

    return nodes


def test_reversing_an_empty_list_returns_none():
    assert Solution().reverseList(None) is None


def test_reversing_a_single_node_returns_the_same_node():
    head, original_nodes = make_linked_list([42])

    reversed_head = Solution().reverseList(head)

    assert reversed_head is original_nodes[0]
    assert reversed_head.val == 42
    assert reversed_head.next is None


def test_reverses_multiple_nodes_in_place():
    head, original_nodes = make_linked_list([1, 2, 3, 4, 5])

    reversed_head = Solution().reverseList(head)
    reversed_nodes = nodes_from(reversed_head)

    assert [node.val for node in reversed_nodes] == [5, 4, 3, 2, 1]
    # Reversal should relink the original nodes instead of creating new ones.
    assert reversed_nodes == original_nodes[::-1]
