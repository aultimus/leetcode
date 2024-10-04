# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverse_node_list(n: ListNode) -> int:
    s = ""
    while True:
        s = str(n.val) + s
        if n.next is None:
            break
        n = n.next
    return int(s)


def create_node_list(n: int) -> ListNode:
    node = ListNode(0, None)
    start = node
    nums = [int(c) for c in str(n)]
    nums.reverse()
    for i in range(0, len(nums)):
        node.val = nums[i]
        if i == len(nums) - 1:
            break
        node.next = ListNode(0, None)
        node = node.next
    return start


def addTwoNumbers(l1: ListNode, l2: ListNode) -> int:

    s1 = traverse_node_list(l1)
    s2 = traverse_node_list(l2)

    total = int(s1) + int(s2)
    return total


def test_simple():
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    assert addTwoNumbers(l1, l2) == 807


def test_create_node_list():
    nl = create_node_list(342)
    n = traverse_node_list(nl)
    assert n == 342


def test_create_node_list_zero():
    nl = create_node_list(0)
    n = traverse_node_list(nl)
    assert n == 0


def test_create_node_list_contains_zero():
    nl = create_node_list(10)
    n = traverse_node_list(nl)
    assert n == 10


def test_complex():
    l1 = create_node_list(9999999)
    l2 = create_node_list(9999)

    assert addTwoNumbers(l1, l2) == 10009998
    assert traverse_node_list(create_node_list(10009998)) == 10009998
