import random


class two_stack_queue(object):
    """
    用两个栈来实现队列的push poll peek功能
    stack_push 用来模拟入队
    stack_pop 用来模拟出队
    注意：
        1,入队时要保证将所有的stack_pop倒入stack_push
        2,出队时要保证将所有的stack_push倒入stack_pop
    """
    def __init__(self):
        self.stack_pop = []
        self.stack_push = []

    def push(self,new_item):
        """
        向队列尾追加元素
        """
        while self.stack_pop:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(new_item)

    def poll(self):
        """
        从队列头取元素
        """
        if not self.stack_pop and not self.stack_push:
            raise Exception('queue is empty')
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self):
        """
        查看队头元素
        """
        if not self.stack_pop and not self.stack_push:
            return None
        if self.stack_pop:
            return self.stack_pop[-1]
        if self.stack_push:
            return self.stack_push[0]

    def empty(self):
        return not self.stack_push and not self.stack_pop

    def __repr__(self):
        if self.empty():
            return ''
        else:
            return str(self.stack_pop[::-1]) if self.stack_pop else str(self.stack_push)


if __name__ == '__main__':
    queue = two_stack_queue()
    for i in range(20):
        queue.push(random.randint(0,20))
    print(queue)
    for i in range(5):
        print('poll:',queue.poll())
    print(queue)
