"""
    合并两个有序单链表
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
    sort_list = sorted([random.randint(0,9) for _ in range(num)])
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for num in sort_list[1:]:
        tail.next = Node(num)
        tail = tail.next
    return dummyhead


def merge_list(head1: Node, head2: Node):
    # 将一个链表合并到另一个链表中
    if head1 is None or head2 is None:
        ret = head1 if head2 is None else head2
        return ret
    head = head1 if head1.val < head2.val else head2
    cur1 = head1 if head1 == head else head2
    cur2 = head2 if head1 == head else head1
    pre, next = None, None
    while cur1 is not None and cur2 is not None:
        if cur1.val <= cur2.val:
            pre = cur1
            cur1 = cur1.next
        else:
            next = cur2.next
            pre.next = cur2
            cur2.next = cur1
            pre = cur2
            cur2 = next
    pre.next = cur1 if cur2 is None else cur2
    return head


if __name__ == '__main__':
    head1 = make_list(10)
    head2 = make_list(10)
    print('---before merge---')
    print_list(head1)
    print_list(head2)
    print('---after merge---')
    head = merge_list(head1, head2)
    print_list(head)






































