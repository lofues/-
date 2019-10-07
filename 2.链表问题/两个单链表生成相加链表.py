"""
    链表的每个节点存储0-9的数字，将两个链表的以此位置相加返回新链表
    例如：1->3->9  + 2->4->1 = 3->8->0
    方法1:
        使用两个栈依次将链表节点压入再相加
    方法2:
        将两个链表逆序后以此相加，再将结果逆序，节省了栈的空间
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


def add_two_list_1(head1:Node, head2:Node):
    """
    方法1
    """
    if head1 is None and head2 is None:
        return head1
    if head1 is None or head2 is None:
        ret = head1 if head1 is not None else head2
        return ret
    s1, s2 = [], []
    while head1 is not None:
        s1.append(head1.val)
        head1 = head1.next
    while head2 is not None:
        s2.append(head2.val)
        head2 = head2.next

    # 申请变量进行头插法
    res = 0  # 每位和
    carry = 0  # 进位
    head, cur = None, None
    while s1 or s2:
        v1 = s1.pop() if s1 else 0
        v2 = s2.pop() if s2 else 0
        res = v1 + v2 + carry
        cur = Node(res % 10)
        cur.next = head
        head = cur
        carry = res // 10
    if carry != 0:
        cur = Node(carry)
        cur.next = head
        head = cur
    return head


def add_two_list_2(head1:Node, head2:Node):
    if head1 is None and head2 is None:
        return head1
    if head1 is None or head2 is None:
        ret = head1 if head1 is not None else head2
        return ret
    # 逆序链表并申请变量
    head1 = reverse_list_iterate(head1)
    head2 = reverse_list_iterate(head2)
    carry, res = 0, 0
    head, cur = None, None
    while head1 is not None or head2 is not None:
        # 将逆序后的两个链表从低位到高位相加
        # 使用头插法自动将结果逆序
        v1 = head1.val if head1 is not None else 0
        v2 = head2.val if head2 is not None else 0
        res = v1 + v2 + carry
        cur = Node(res % 10)
        cur.next = head
        head = cur
        carry = res // 10
        head1 = head1.next if head1 is not None else None
        head2 = head2.next if head2 is not None else None
    if carry != 0:
        cur = Node(carry)
        cur.next = head
        head = cur
    return head


def reverse_list_recursive(head: Node):
    if head is None or head.next is None:
        return head
    last = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_list_iterate(head: Node):
    if head is None or head.next is None:
        return head
    pre, cur = None, head
    while cur is not None:
        post = cur.next
        cur.next = pre
        pre, cur = cur, post
    return pre


if __name__ == '__main__':
    list_1 = make_list(5)
    list_2 = make_list(10)
    print('---before add---')
    print_list(list_1)
    print_list(list_2)
    print('---after add---')
    list_add = add_two_list_2(list_1, list_2)
    print_list(list_add)









