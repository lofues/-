"""
    有两个有序的公共链表，打印出两个链表的公共部分
    解法：
        从head1 和 head2进行遍历
        1,若head1.val < head2.val 则head1向下移动
        2,若head2.val < head1.val 则head2向下移动
        3,若head1.val = head2.val 则打印公共节点，并同时移动head1和head2
"""
import random


class Node(object):
    def __init__(self,val = None):
        self.val = val
        self.next = None


def print_common_part(head1, head2):
    if head1 is None or head2 is None:
        return
    while head1 and head2:
        if head1.val < head2.val:
            head1 = head1.next
        elif head2.val < head1.val:
            head2 = head2.next
        else:
            print(head1.val, end='  ')
            head1 = head1.next
            head2 = head2.next


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


if __name__ == '__main__':
    list1 = make_list(10)
    print('---list1---')
    print_list(list1)

    list2 = make_list(10)
    print('---list2---')
    print_list(list2)

    print('---common part---')
    print_common_part(list1, list2)






