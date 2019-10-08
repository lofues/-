"""
    有一种怪异的节点删除方式：只给被删除的节点，要求删除该节点（节点内存储的只有一个整数值）
    方法：
        将下一个节点的值复制到该节点然后删除下一个节点
    缺点：
        无法删除最后一个节点-> 若删除的是最后一个节点要抛出异常
        若节点内存储的数据较大或者存在各种与其他类、函数等的依赖关系则无法实现
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


def weird_delete_node(node: Node):
    if node is None:
        return node
    if node.next is not None:
        next = node.next
        node.val = next.val
        node.next = next.next
    else:
        raise Exception('can`t delete the last node')


def find_kth_node(head: Node, k: int):
    if head is None:
        return head
    cur = head
    while cur is not None:
        k -= 1
        if k == 0:
            return cur
        cur = cur.next
    raise Exception('there isn`t that much nodes')


if __name__ == '__main__':
    list_1 = make_list(10)
    print('---before delete node---')
    print_list(list_1)
    kth = random.randint(1, 10)
    node = find_kth_node(list_1, kth)
    weird_delete_node(node)
    print('---after delete node---')
    print_list(list_1)


















