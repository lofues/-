"""
    一个循环链表，每次遍历到第m个节点时便删除该节点，之后从该节点之后循环遍历到第m个节点并删除
    返回最后剩余的一个节点，并自成循环链表
"""

import random


class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None


def print_list_circle(head):
    if head is None:
        return
    cur = head
    print(cur.val, end='  ')
    while cur.next != head:
        cur = cur.next
        print(cur.val, end='  ')
    print()


def make_list_circle(num):
    sort_list = sorted([random.randint(0,20) for _ in range(num)])
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for i in sort_list[1:]:
        tail.next = Node(i)
        tail = tail.next
    tail.next = dummyhead
    return dummyhead


def josephus_kill(head, m: int):
    if head is None or m < 1:
        return head
    last = head
    while last.next != head:
        last = last.next
    count = 0
    while last != head:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = last.next
        # head一直保持在last的下一个节点，用来判断链表长度
        head = last.next
    return head


if __name__ == '__main__':
    head = make_list_circle(10)
    print('---before josephus---')
    print_list_circle(head)
    head = josephus_kill(head,2)
    print('---after josephus 2---')
    print_list_circle(head)






