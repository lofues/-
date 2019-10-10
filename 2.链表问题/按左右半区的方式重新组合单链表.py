"""
    按照左右半区的方式重新组合单链表
        若为奇数个数，则n // 2 为左半区 n // 2 + 1 为右半区
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
        print(dummyhead.val, end='  ')
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


def re_locate(head: Node):
    if head is None or head.next is None:
        return head
    # mid 为中间节点
    mid = head
    # right为右半区链表的头结点
    right = head.next
    while right.next is not None and right.next.next is not None:
        mid = mid.next
        right = right.next.next
    # 将right置为右半区的中间节点
    right = mid.next
    # 左右半区分离
    mid.next = None
    cat_left_and_right(head, right)


def cat_left_and_right(left: Node, right: Node):
    next = None
    while left.next is not None:
        next = right.next
        right.next = left.next
        left.next = right
        left = right.next
        right = next
    left.next = right


if __name__ == '__main__':
    list_1 = make_list(11)
    print('---before relocate---')
    print_list(list_1)
    print('---after relocate---')
    re_locate(list_1)
    print_list(list_1)









