"""
    反转单向链表的部分节点
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


def reverse_part_list(head, From: int, To: int):
    # 先找到第From-1的节点 和 To+1的节点
    n = 0
    fpre = None
    tpost = None
    cur = head
    while cur is not None:
        n += 1
        fpre = cur if n == From - 1 else fpre
        tpost = cur if n == To + 1 else tpost
        cur = cur.next
    # 处理反转部分的第一个节点，使其连接tpost
    cur = head if fpre is None else fpre.next
    post = cur.next
    post_post = None
    cur.next = tpost
    # 反转链表
    while post != tpost:
        post_post = post.next
        post.next = cur
        cur, post = post, post_post
    if fpre is not None:
        fpre.next = cur
        return head
    else:
        return cur


if __name__ == '__main__':
    head = make_list(10)
    print('---before remove---')
    print_list(head)
    print('---after reverse 1 to 3---')
    head = reverse_part_list(head, 1, 3)
    print_list(head)
    print('---after reverse 2 to 5---')
    head = reverse_part_list(head, 2, 5)
    print_list(head)







































