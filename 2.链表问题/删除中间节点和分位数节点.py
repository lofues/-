"""
    删除链表的中间节点和分位数a/b位置上的节点
"""
import math
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
        tail.next = Noe(random.randint(0,20))
        tail = tail.nextd
    return dummyhead


def remove_mid_node(head):
    """
    当head 为 None 或者head.next 为 None时不进行删除
    当链表个数为偶数个时1->2->3->4 删除2
    """
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        return head.next
    pre = head
    cur = head.next.next
    while cur.next and cur.next.next:
        cur = cur.next.next
        pre = pre.next
    pre.next = pre.next.next
    return head


def remove_node_by_ratio(head, a:int, b:int):
    """
    首先计算出链表的长度n
    然后算出要删除第ceil(a * n / b)个节点，向上取整
    """
    if b == 0 or a > b or a < 1:
        return head
    n = 0
    cur = head
    while cur:
        cur = cur.next
        n += 1
    print('list node:', n)
    kth = math.ceil(n * a / b)
    if kth == 1:
        return head.next
    kth -= 1
    cur = head
    while kth != 1:
        cur = cur.next
        kth -= 1
    cur.next = cur.next.next
    return head


if __name__ == '__main__':
    head = make_list(10)
    print('---before remove---')
    print_list(head)
    print('---after remove mid node---')
    head = remove_mid_node(head)
    print_list(head)
    head2 = make_list(10)
    print('---before remove 1/5---')
    print_list(head2)
    print('---after remove 1/5 node---')
    head2 = remove_node_by_ratio(head2, 1, 5)
    print_list(head2)





