"""
    实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作

    要求：
    1.pop push getMin时间复杂度都为O(1)
    2.设计的栈类型可以使用现成的栈结构
"""
import random
class Stack_1(object):
    """
    第一种设计方法
    设计两个栈：正常的栈stack 存储每一步最小值的栈stack_min
    1,压入规则：如果stack_min为空就同时压入两个栈，如果非空，若当前元素小于等于
stack_min的栈顶元素则同时压入两个栈，其余都只压入stack
    2,弹出规则：若stack不为空，弹出stack栈顶元素，若与stack_min相等则同时弹出
    3,得到最小元素：取出stack_min的栈顶
    """
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self,new_item):
        assert type(new_item) is int
        self.stack.append(new_item)
        if not self.stack_min:
            self.stack_min.append(new_item)
        elif new_item <= self.stack_min[-1]:
            self.stack_min.append(new_item)

    def pop(self):
        if not self.stack:
            raise Exception('stack is empty')
        item = self.stack.pop()
        if item == self.stack_min[-1]:
            self.stack_min.pop()
        return item

    def get_min(self):
        if not self.stack_min:
            raise Exception('stack is empty')
        return self.stack_min[-1]

    def __repr__(self):
        return str(self.stack) + '---min_stack---' + str(self.stack_min)

class Stack_2(object):
    """
    第二种实现方法：
    同样有stack 与 stack_min两个栈
    1,压入规则:当前元素为new_item 若stack_min为空则同时压入两栈；若非空，则比较new_item与stack_min栈顶大小，
    若new_item更小则同时压入，若new_item大则在stack_min中重复压入当前栈顶，这样stack_min的栈顶一直保持最小。
    2,弹出规则:同时弹出stack与stack_min栈顶
    3,得到最小元素：取出stack_min栈顶
    """
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self,new_item):
        assert type(new_item) is int
        self.stack.append(new_item)
        if not self.stack_min:
            self.stack_min.append(new_item)
        else:
            if new_item <= self.stack_min[-1]:
                self.stack_min.append(new_item)
            else:
                self.stack_min.append(self.stack_min[-1])

    def pop(self):
        if not self.stack:
            raise Exception('stack is empty')
        self.stack_min.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.stack:
            raise Exception('stack is empty')
        return self.stack_min[-1]

    def __repr__(self):
        return str(self.stack) + '---min_stack----' + str(self.stack_min)

if __name__ == '__main__':
    stack1 = Stack_1()
    stack2 = Stack_2()
    for i in range(10):
        x = random.randint(0,10)
        stack1.push(x)
        stack2.push(x)
    print('----------------------')
    print(stack1)
    print(stack2)
    print('----------------------')
    print('pop:',stack1.pop(),stack2.pop())
    print('min:',stack1.get_min(),stack2.get_min())
    print('pop:',stack1.pop(),stack2.pop())
    print('min:',stack1.get_min(),stack2.get_min())
























