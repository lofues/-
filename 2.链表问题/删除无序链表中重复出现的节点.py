"""
    删除无序链表中重复出现的节点
    方法1:
        利用哈希表，若不存在就加入哈希表，若存在则删除
        时间复杂度O(N) 空间复杂度O(N)
    方法2:
        使用类似选择排序的方法，将重复的删除
        时间复杂度O(N²) 空间复杂度O(1)
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


def deduplicate_list(head: Node):
    """
    pre指向上一次不被删除的节点
    """
    if head is None:
        return head
    d = {}
    d[head.val] = ''
    pre, cur = head, head.next
    while cur is not None:
        if cur.val in d:
            pre.next = cur.next
        else:
            d[cur.val] = ''
            pre = cur
        cur = cur.next


def deduplicate_list_2(head: Node):
    if head is None:
        return head
    pivot = head
    while pivot.next is not None:
        pre, cur = pivot, pivot.next
        while cur is not None:
            if cur.val == pivot.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        pivot = pivot.next


if __name__ == '__main__':
    head = make_list(10)
    print('---before deduplicate---')
    print_list(head)
    print('---after deduplicate---')
    deduplicate_list_2(head)
    print_list(head)





























