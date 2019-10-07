"""
    基本要求时间复杂度O(N),空间复杂度O(N)
    进阶要求时间复杂度O(N),空间复杂度O(1)
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


def list_partion_space_n(head:Node, pivot:int):
    """
        基本要求的解法：
        申请一个节点数组进行一次数组的partion操作，然后以此将链表的指针相连
    """
    if head is None:
        return head
    result = []
    cur = head
    while cur is not None:
        result.append(cur)
        cur = cur.next
    partion_list_space_n(result, pivot)
    for i in range(len(result)-1):
        result[i].next = result[i+1]
    result[-1].next = None
    return result[0]


def partion_list_space_n(arr:list, pivot:int):
    small, big = -1, len(arr)
    index = 0
    while index < big:
        if arr[index].val < pivot:
            small += 1
            arr[small], arr[index] = arr[index], arr[small]
            index += 1
        elif arr[index].val > pivot:
            big -= 1
            arr[big], arr[index] = arr[index], arr[big]
        else:
            index += 1


def partion_list_space_1(head:Node, pivot:int):
    """
    进阶解法：
        将所有节点依次装进小于、等于、大于的三个链表中，再对每个链表的头尾相连
    """
    if head is None:
        return head
    sh, st = None, None # 小于pivot的链表头和尾
    eh, et = None, None # 等于pivot的链表头和尾
    bh, bt = None, None # 大于pivot的链表头和尾
    while head is not None:
        # 注意将每个节点的next指针先置空
        next = head.next
        head.next = None
        if head.val < pivot:
            if sh is None:
                sh = head
                st = head
            else:
                st.next = head
                st = head
        elif head.val == pivot:
            if eh is None:
                eh = head
                et = head
            else:
                et.next = head
                et = head
        else:
            if bh is None:
                bh = head
                bt = head
            else:
                bt.next = head
                bt = head
        head = next
    if st is not None:
        st.next = eh
        et = st if et is None else et
    if et is not None:
        et.next = bh
    if sh is not None:
        return sh
    elif eh is not None:
        return eh
    else:
        return bh


if __name__ == '__main__':
    head = make_list(10)
    print('---before partion---')
    print_list(head)
    print('---after partion 10---')
    # head = list_partion_space_n(head, 10)
    head = partion_list_space_1(head, 10)
    print_list(head)