"""
    使用不同方式实现二叉树的前中后序遍历
"""

import random


class TreeNode(object):
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

def make_tree(num):
    arr = [random.randint(0,9) for _ in range(num)]
    return _list_make_tree(None, arr, 0)


def _list_make_tree(root:TreeNode, arr:list, i:int):
    if i < len(arr):
        if arr[i] == '#':
            return None
        else:
            root = TreeNode(arr[i])
            root.left = _list_make_tree(root.left, arr, 2*i+1)
            root.right = _list_make_tree(root.right, arr, 2*i+2)
            return root
    else:
        return None


def print_tree(root: TreeNode):
    if root is None:
        return
    queue = [(root, 1)]
    cur_floor = 1
    while queue:
        cur, floor = queue.pop(0)
        if floor > cur_floor:
            cur_floor = floor
            print()
        print(cur.val, sep='  ', end='  ')
        if cur.left:
            queue.append((cur.left, floor+1))
        if cur.right:
            queue.append((cur.right, floor+1))
    print()


def pre_order_rec(root: TreeNode):
    if root is None:
        return
    print(root.val, end='  ')
    pre_order_rec(root.left)
    pre_order_rec(root.right)


def in_order_rec(root: TreeNode):
    if root is None:
        return
    in_order_rec(root.left)
    print(root.val, end='  ')
    in_order_rec(root.right)


def post_order_rec(root: TreeNode):
    if root is None:
        return
    post_order_rec(root.left)
    post_order_rec(root.right)
    print(root.val, end='  ')


def pre_order_iter(root:TreeNode):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end='  ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print()


def in_order_iter(root: TreeNode):
    # 循环遍历左儿子，若左儿子为空则打印并遍历右儿子   之后重复
    if root is None:
        return
    stack = []
    while stack or root is not None:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val, end='  ')
            root = root.right
    print()


def post_order_iter(root: TreeNode):
    # 使用两个栈模拟 左 右 根
    stack1, stack2 = [root], []
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        if root.left is not None:
            stack1.append(root.left)
        if root.right is not None:
            stack1.append(root.right)
    while stack2:
        root = stack2.pop()
        print(root.val, end='  ')
    print()


if __name__ == '__main__':
    root = make_tree(10)
    print('---tree picture---')
    print_tree(root)
    print('---pre in post---')
    pre_order_rec(root)
    print()
    pre_order_iter(root)
    in_order_rec(root)
    print()
    in_order_iter(root)
    post_order_rec(root)
    print()
    post_order_iter(root)





































