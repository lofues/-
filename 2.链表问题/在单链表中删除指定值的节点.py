"""
    在单链表中删除指定值的节点
    方法1：
        使用栈将非指定值的节点压入栈中
        时间复杂度 O(N) 空间复杂度O(N)
    方法2:
        原地删除，注意要先找到第一个非指定值的节点作为头结点
        时间复杂度O(N) 空间复杂度O(1)
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


def delete_node_1(head: Node, key: int):
    if head is None or not isinstance(key, int):
        return head
    stack = []
    while head is not None:
        if head.val != key:
            stack.append(head)
        head = head.next
    cur = None
    if stack:
        while stack:
            cur = stack.pop()
            if stack:
                stack[-1].next = cur
    return cur


def delete_node_2(head: Node, key: int):
    if head is None or not isinstance(key, int):
        return head
    new_head = head
    while new_head is not None and new_head.val == key:
        new_head = new_head.next
    if new_head is not None:
        pre, cur = new_head, new_head.next
        while cur is not None:
            if cur.val == key:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
    return new_head


if __name__ == '__main__':
    list_1 = make_list(10)
    cur = list_1
    new_head = Node(5)
    new_head.next = list_1
    list_1 = new_head
    new_head = Node(3)
    new_head.next = list_1
    print('---before delete 3---')
    print_list(new_head)
    print('---after delete 3---')
    new_head = delete_node_1(new_head, 3)
    print_list(new_head)
    print('---after delete 5---')
    new_head = delete_node_2(new_head, 5)
    print_list(new_head)




























