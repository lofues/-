"""
    要求：一个栈中元素的类型为整形，现要将该栈从顶到底从大到小的顺序排序，只许申请一个栈。可以申请新的变量，但不能申请额外的数据结构。
    解法：
        设要求排序的栈为sort 辅助栈为help 从sort中弹出的栈顶元素为cur
        1,如果cur小于help的栈顶元素，则压入到help栈中
        2,如果cur大于help的栈顶元素，则将help的元素以此倒入sort中重复弹出
"""
import random


def sort_queue_by_queue(stack):
    if not stack:
        return
    help = []
    while stack:
        item = stack.pop()
        while help and item > help[-1]:
            stack.append(help.pop())
        help.append(item)
    while help:
        stack.append(help.pop())



if __name__ == '__main__':
    stack = []
    for i in range(10):
        stack.append(random.randint(0,100))
    print(stack)
    print('-----after sort-----')
    sort_queue_by_queue(stack)
    print(stack)