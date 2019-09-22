"""
    逆序一个栈：实现两个递归函数
    1->每次从栈中取出最低层的元素
    2->实现一个递归将取出最底层的最底层元素按后来先执行的顺序插入到栈中
"""
import random


def get_last_and_remove(stack):
    """
    从栈中取出并删除栈底元素
    """
    item = stack.pop()
    if not stack:
        return item
    else:
        last = get_last_and_remove(stack)
        stack.append(item)
        return last

def reverse(stack):
    """
    对栈进行逆序
    """
    if not stack:
        return
    else:
        last = get_last_and_remove(stack)
        reverse(stack)
        stack.append(last)
if __name__ == '__main__':
    stack = []
    # 测试get_last_and_remove
    for i in range(5):
        stack.append(random.randint(0,10))
    print(stack)
    print('bottom:',get_last_and_remove(stack))
    print(stack)

    # 测试reverse
    reverse(stack)
    print(stack)