"""
    给一个数组arr，求出所有arr的子数组的最大值减去最小值小于等于num的数量
    暴力方法：
        1，在O(n²)的时间复杂度下找出所有的子数组
        2，在每个子数组中找出最大值和最小值并计算O(n)
        3，总时间复杂度O(n³)
    最优解：
        1，维持最大值和最小值的双端队列（参考滑动窗口的最大值数组）
        2，i<j 两个指针遍历arr找出以arr[i]为开头的数组个数j-i
        3，将所有的j-i进行相加;每个元素分别进出一次队列并判断，总时间复杂度O(n)
"""
import random


def get_max(arr: list, num : int):
    if not arr or len(arr) == 0 or num < 0:
        return 0
    qmax, qmin = [], []
    i = 0
    j = 0
    ret = 0
    while i < len(arr):
        while j < len(arr):
            if not qmin or qmin[-1] != j:
                while qmin and arr[qmin[-1]] >= arr[j]:
                    qmin.pop()
                qmin.append(j)
                while qmax and arr[qmax[-1]] <= arr[j]:
                    qmax.pop()
                qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        ret += j - i
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        i += 1

    return ret


if __name__ == '__main__':
    test = [random.randint(1,20) for _ in range(3)]
    print(test)
    print('----get max number---')
    print(get_max(test,5))



