"""
    判断一个链表是否是回文结构
    方法1：
        借助栈结构进行逆序
        时间复杂度： O(n) 空间复杂度O(n)
    方法2
        对方法1进行优化，只将右半部分的节点压入栈中

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


def make_list_palindrome():
    sort_list = [1,2,3,2,1]
    dummyhead = Node(sort_list[0])
    tail = dummyhead
    for i in sort_list[1:]:
        tail.next = Node(i)
        tail = tail.next
    return dummyhead


def is_palindrome_1(head):
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur)
        cur = cur.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True


def is_palindrome_2(head):
    if head is None or head.next is None:
        return True
    stack = []
    right = head.next
    cur = head
    while cur.next and cur.next.next:
        right = right.next
        cur = cur.next.next
    while right is not None:
        stack.append(right)
        right = right.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True


if __name__ == '__main__':
    head = make_list_palindrome()
    print(is_palindrome_1(head))
    print(is_palindrome_2(head))







