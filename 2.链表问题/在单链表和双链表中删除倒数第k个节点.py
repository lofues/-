"""
    分别实现两个函数：一个可以删除单链表的倒数第k个节点，一个可以删除双链表的倒数第k个节点
"""


import random


class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None


class DoubNode(object):
    def __init__(self, val=None):
        self.val = val
        self.pre = None
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
        tail.next = Node(i)
        tail = tail.next
    return dummyhead


def remove_last_kth_node_single_list(head, k):
    """
        先遍历到链表尾，每次遍历k 减去 1
        若 k == 0,则要删除第一个节点
        若 k < 0,则重复从头结点向右遍历，每次加1，则k==0时 刚好是第n-k个节点即要删除的前一个节点
    """
    if head is None or k < 1:
        return head
    cur = head
    while cur:
        cur = cur.next
        k -= 1
    if k == 0:
        return head.next
    if k < 0:
        cur = head
        # 先进行加1，此时再遍历到k==0时，节点为第n-k-1，即倒数第k+1个
        k += 1
        while k != 0:
            cur = cur.next
            k += 1
        cur.next = cur.next.next

    return head


def remove_last_kth_node_double_list(head, k):
    """
        对于双链表的处理与单链表的处理一致
    """
    if head is None or k < 1:
        return head
    cur = head
    while cur:
        cur = cur.next
        k -= 1
    if k == 0:
        head = head.next
        head.pre = None
    if k < 0:
        cur = head
        # 先加1，之后遍历到k == 0时，为第n-k-1的节点
        k += 1
        while k != 0:
            cur = cur.next
            k += 1
        cur.next = cur.next.next
        # 注意cur.next可能为空
        if cur.next:
            cur.next.pre = cur
    return head


if __name__ == '__main__':
    head = make_list(10)
    print('---single list---')
    print_list(head)
    print('---after delete last 3th---')
    head = remove_last_kth_node_single_list(head, 11)
    print_list(head)











































