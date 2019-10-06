"""
    反转单向和双向链表
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
    sort_list = sorted([random.randint(0,20) for _ in range(num)])
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for i in sort_list[1:]:
        tail.next = Node(random.randint(0,20))
        tail = tail.next
    return dummyhead


def reverse_single_list_recursive(head):
    if head is None or head.next is None:
        return head
    last = reverse_single_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_single_list_iterate(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    while cur is not None:
        post = cur.next
        cur.next = pre
        pre, cur = cur, post
    return pre


def reverse_double_list_iterate(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    while cur is not None:
        post = cur.next
        cur.pre = post
        cur.next = pre
        pre, cur = cur, post
    return pre


if __name__ == '__main__':
    head1 = make_list(10)
    print('---before reverse---')
    print_list(head1)
    head1 = reverse_single_list_recursive(head1)
    print('---after reverse---')
    print_list(head1)
    head1 = reverse_single_list_iterate(head1)
    print_list(head1)















































