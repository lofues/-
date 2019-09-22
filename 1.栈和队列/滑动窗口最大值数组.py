"""
    有一个数组形如:[3,1,5,7,3,5,2] 滑动窗口长度为3 如[3,1,5],[1,5,7]....
    要求：
        在O(n)复杂度内求出每个滑动窗口的最大值并保存在数组ret中
    方法：
        模拟一个单调递减的双端队列，保证队列中的元素始终在滑动窗口的范围内，队头的元素即是最大值

        依次遍历数组arr，维护一个qmax双端队列保存数组元素的下标，其中队头是窗口最大值的下标，push和poll方法如下
            假设遍历到arr[i]
            push：
                当qmax为空时push;
                当qmax不为空时，若队尾元素下标j指向的值arr[j]>arr[i]则push；若arr[j]<arr[i]则循环弹出队尾元素直到arr[j]>arr[i],push
            poll:
                当队头元素下标j小于滑动窗口的头下标i-w+1则弹出;否则添加到ret中
"""
import random


def get_max_window(arr:list, w:int):
    if not arr or len(arr) < w or w < 1:
        return []
    ret = []
    qmax = []
    for i in range(len(arr)):
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] <= i - w:
            qmax.pop(0)
        if i >= w-1:
            index = qmax[0]
            ret.append(arr[index])
    return ret

if __name__ == '__main__':
    test = []
    for i in range(10):
        test.append(random.randint(0,100))
    print(test)
    print('----after get max window----')
    print(get_max_window(test,4))
















