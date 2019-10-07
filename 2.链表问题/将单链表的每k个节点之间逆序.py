"""
    将单链表每k个节点之间进行逆序，最后不足k的不进行逆序
    方法1：
        使用栈结构   时间复杂度O(N), 空间复杂度O(K)
    方法2:
        不使用栈结构，记录k个节点的开始和结束     时间复杂度O(N), 空间复杂度O(1)
"""
import random


class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None


def print_list(head):
    if head is None:
        return
    dummyhead = head
    while dummyhead:
        print(dummyhead.val,end='  ')
        dummyhead = dummyhead.next
    print()


def make_list(num):
    sort_list = [random.randint(0,9) for _ in range(num)]
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for num in sort_list[1:]:
        tail.next = Node(num)
        tail = tail.next
    return dummyhead


def reverse_k_node(head: Node, k: int):
    if head is None or k < 2:
        return head
    stack = []
    new_head = head
    cur = head
    pre, next = None, None
    while cur is not None:
        next = cur.next
        stack.append(cur)
        if len(stack) == k:
            pre = parse_stack_reverse(stack, pre, next)
            new_head = cur if new_head == head else new_head
        cur = next
    return new_head


def parse_stack_reverse(stack: list, left: Node, right: Node):
    cur = stack.pop()
    if left is not None:
        left.next = cur
    while stack:
        next = stack.pop()
        cur.next = next
        cur = next
    cur.next = right
    return cur


def reverse_k_node_2(head: Node, k: int):
    if head is None or k < 2:
        return head
    new_head = head
    pre, cur = None, head
    count = 0
    while cur is not None:
        count += 1
        next = cur.next
        if count == 3:
            count = 0
            new_head = cur if new_head == head else new_head
            start = pre.next if pre is not None else head
            pre = parse_node(pre, start, cur, next)
        cur = next
    return new_head


def parse_node(left: Node, start: Node, end: Node, right: Node):
    pre, cur = None, start
    while cur != right:
        next = cur.next
        cur.next = pre
        pre, cur = cur, next
    if left is not None:
        left.next = end
    start.next = right
    return start


if __name__ == '__main__':
    list_1 = make_list(10)
    print('---before 3 reverse---')
    print_list(list_1)
    print('---after 3 reverse---')
    list_1 = reverse_k_node(list_1, 3)
    print_list(list_1)
    print('---after 3 reverse again---')
    list_1 = reverse_k_node_2(list_1, 3)
    print_list(list_1)


























