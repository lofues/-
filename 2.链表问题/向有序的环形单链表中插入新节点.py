"""
    向有序的环形单链表中插入新节点
    注意：若该节点值大于所有节点要插入到最后一个位置
         若该节点值小于所有节点，需要更换新的头结点
         若链表为空则返回单个的环形链表
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
    print(dummyhead.val, end='  ')
    dummyhead = dummyhead.next
    while dummyhead != head:
        print(dummyhead.val, end='  ')
        dummyhead = dummyhead.next
    print()


def make_list(num):
    sort_list = sorted([random.randint(0,9) for _ in range(num)])
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for num in sort_list[1:]:
        tail.next = Node(num)
        tail = tail.next
    tail.next = dummyhead
    return dummyhead


def insert_node_into_circle_list(head: Node, value: int):
    node = Node(value)
    if head is None:
        node.next = node
        return node
    pre, cur = head, head.next
    while cur != head:
        if pre.val <= value <= cur.val:
            break
        pre, cur = cur, cur.next
    # 不管是在尾部添加节点还是在链表之间添加节点都是共同的操作
    pre.next = node
    node.next = cur
    if value < head.val:
        head = node
    return head


if __name__ == '__main__':
    list_1 = make_list(10)
    print('---before insert node---')
    print_list(list_1)
    print('---after insert node---')
    list_1 = insert_node_into_circle_list(list_1, 10)
    list_1 = insert_node_into_circle_list(list_1, 0)
    print_list(list_1)




















