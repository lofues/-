"""
    要求实现单链表的选择排序
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


def select_sort_list(head: Node):
    small_pre = None  # 最小值节点的前驱
    small = None  # 最小值的节点
    cur = head  # 无序链表的头结点
    tail = None  # 有序链表的尾节点
    while cur is not None:
        small = cur
        small_pre = find_small_pre(cur)
        # 如果small 节点不是 cur
        if small_pre is not None:
            small = small_pre.next
            small_pre.next = small.next
        # 如果small 节点是 cur
        cur = cur.next if small == cur else cur
        # 将small 节点连接到有序链表之后
        if tail is None:
            head = small
            tail = head
        else:
            tail.next = small
            tail = small
    return head


def find_small_pre(head: Node):
    small_pre = None
    small = head
    pre = head
    cur = head.next
    while cur is not None:
        if cur.val < small.val:
            small_pre = pre
            small = cur
        pre, cur = cur, cur.next
    return small_pre


if __name__ == '__main__':
    list_1 = make_list(10)
    print('---before sort---')
    print_list(list_1)
    print('---after sort---')
    list_1 = select_sort_list(list_1)
    print_list(list_1)





















