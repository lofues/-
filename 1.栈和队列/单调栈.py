"""
    给定一个不含有重复值的数组arr，找到每一个i位置左边和右边距离i位置最近且值比arr[i]小的位置，返回所有位置相应的信息
    例如:
        arr = [3, 4, 1, 5, 6, 2, 7]
        ret = [
            (-1, 2),
            (0, 2),
            (-1, -1),
            (2, 5),
            (3, 5),
            (2, -1),
            (5, -1)
        ]
    基本：要求O(n)的时间复杂度
    进阶：数组arr包含重复元素

"""

# 首先是O(n²)的解法
def parse_simple(arr : list):
    ret = []
    for i,val in enumerate(arr):
        left_index = -1
        right_index = -1
        cur_index = i - 1
        while cur_index >= 0 :
            if arr[cur_index] < arr[i]:
                left_index = cur_index
                break
            cur_index -= 1
        cur_index = i + 1
        while cur_index <= len(arr) - 1:
            if arr[cur_index] < arr[i]:
                right_index = cur_index
                break
            cur_index += 1
        ret.append((left_index,right_index))
    return ret


# 下面是O(n)的解法
def parse_complex(arr : list):
    """
    维持单调栈的结构：栈顶到栈底单调递减
    当遍历到i位置时：
        1，如果栈为空就push
        2，如果栈顶位置的值小于arr[i],就push
        3，如果栈顶位置的值小于arr[i]，则栈顶位置下边的值就是栈顶位置左边最近且比栈顶小的值，i就是栈顶位置右边最近且比栈顶小的值
    遍历完成后，若栈不空则以此弹出栈中元素并按照上边所述规则进行处理
    """

    stack = []
    ret = [() for _ in range(len(arr))]
    for i,val in enumerate(arr):
        while stack and arr[stack[-1]] > arr[i]:
            cur_index = stack.pop()
            left_index = stack[-1] if stack else -1
            right_index = i
            ret[cur_index] = (left_index, right_index)
        stack.append(i)
    while stack:
        cur_index = stack.pop()
        left_index = stack[-1] if stack else -1
        right_index = -1
        ret[cur_index] = (left_index, right_index)
    return ret


# 下面是进阶解法
def parse_complex_duplicate(arr : list):
    """
    解法与原方法一致，只不过在push元素时要对相等元素进行判断，如果与栈顶元素相等需要将元素压入栈顶元素内
    在pop元素时有可能pop的是多个元素，此时需要对多个元素的前后位置进行判断，pop完栈顶后，如果栈中还有元素则左边位置即是栈顶的最后一个元素，否则是-1
    """
    ret = [() for _ in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        if not stack or arr[i] > arr[stack[-1][-1]]:
            stack.append([i])
        elif arr[i] == arr[stack[-1][-1]]:
            stack[-1].append(i)
        else:
            while stack and arr[i] < arr[stack[-1][-1]]:
                cur_indexs = stack.pop()
                left_index = stack[-1][-1] if stack else -1
                right_index = i
                for cur_index in cur_indexs:
                    ret[cur_index] = (left_index,right_index)
            if not stack:
                stack.append([i])
            else:
                if arr[stack[-1][-1]] == arr[i]:
                    stack[-1].append(i)
                else:
                    stack.append([i])
    while stack:
        cur_indexs = stack.pop()
        left_index = stack[-1][-1] if stack else - 1
        right_index = -1
        for cur_index in cur_indexs:
            ret[cur_index] = (left_index, right_index)
    return ret


if __name__ == '__main__':
    arr = [3, 4, 1, 5, 6, 2, 7]
    print(parse_simple(arr))
    print('----parse_complex-----')
    print(parse_complex(arr))
    arr_duplicate = [3, 1, 3, 4, 3, 5, 3, 2, 2]
    print('----parse_complex_duplicate----')
    print(parse_complex_duplicate(arr_duplicate))
























