"""
    将二叉搜索树转换为有序双向链表,树的left和right相当于双向链表的pre和next
    方法1：
        使用队列将二叉搜索树的中序遍历搜集起来，然后依次连接
        时间复杂度O(N) 空间复杂度O(N)
    方法2：
        使用递归函数，返回有序双向链表的头结点和尾节点 递归实现左子树的有序双向链表然后实现右子树，最后左右的头尾相连
        时间复杂度O(N) 空间复杂度O(h) h为递归栈深度，即二叉树的高度
"""
import random


class TreeNode(object):
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None


def binary_search_tree_to_double_list_1(root: TreeNode):
    if root is None:
        return root
    queue = []
    in_order(root, queue)
    head = queue.pop(0)
    pre = head
    pre.left = None
    cur = None
    while queue:
        cur = queue.pop(0)
        cur.left = pre
        pre.right = cur
        pre = cur
    pre.right = None
    return head


def binary_search_tree_to_double_list_2(head):
    if head is None:
        return head
    return _binary_search_tree_to_double_list_2(head)[0]


def _binary_search_tree_to_double_list_2(head):
    # 返回值为双向链表的头结点和尾节点 ： start  end
    if head is None:
        return None, None
    left_list = _binary_search_tree_to_double_list_2(head.left)
    right_list = _binary_search_tree_to_double_list_2(head.right)
    if left_list[1] is not None:
        left_list[1].right = head
    head.left = left_list[1]
    head.right = right_list[0]
    if right_list[0] is not None:
        right_list[0].left = head
    start = left_list[0] if left_list[0] is not None else head
    end = right_list[1] if right_list[1] is not None else head
    return start, end


def in_order(root: TreeNode, queue: list):
    if root is None:
        return
    in_order(root.left, queue)
    queue.append(root)
    in_order(root.right, queue)


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


if __name__ == '__main__':
    root = make_tree(20)
    print_tree(root)































