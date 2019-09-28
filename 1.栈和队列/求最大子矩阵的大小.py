"""
    题目描述：
        有一个二维数组分别有1 和 0组成，求1所能表示的矩形的最大面积
        例如：
            map = 1 0 1 1 1 1
                  1 1 1 1 1 1
                  1 1 1 0 1 0
            最大矩形面积为8
"""


def get_max_area(map_list):
    """
        首先求出每一个位置上列的连续1个数height[i][j]
        然后对每一行的height使用单调栈方法求出该行位置上的最大面积
    """
    # 存储每行的最大面积
    ret = []
    heights = [[0 for col in range(len(map_list[0]))] for row in range(len(map_list))]
    for row in range(len(map_list)):
        for col in range(len(map_list[0])):
            if row == 0:
                heights[row][col] = 1 if map_list[row][col] else 0
            else:
                heights[row][col] = heights[row-1][col] + 1 if map_list[row][col] else 0
    for height in heights:
        ret.append(get_max_area_by_height(height))
    print(ret)
    return max(ret)


def get_max_area_by_height(height):
    """
    根据单调栈方法求出该行最大的面积
    依次遍历height并压栈，当遍历到i位置时：
        若栈为空则进栈
        若height[i]大于栈顶j的height[j]也进栈
    出栈：
        若height[i]<=height[j]，则循环弹出j并计算j位置下的面积，设弹出后栈顶为k
    面积计算方法：
        area[j] = height[j] * (i -k -1)
    """
    areas = [0 for _ in range(len(height))]
    stack = []
    for i in range(len(height)):
        if not stack:
            stack.append(i)
        elif height[i] > height[stack[-1]]:
            stack.append(i)
        else:
            while stack and height[i] <= height[stack[-1]]:
                cur_index = stack.pop()
                left_index = stack[-1] if stack else -1
                right_index = i
                areas[cur_index] = height[cur_index] * (right_index - left_index - 1)
            stack.append(i)

    # 计算栈中剩余位置下的最大面积 此时right_index = len(height)
    while stack:
        cur_index = stack.pop()
        right_index = len(height)
        left_index = stack[-1] if stack else -1
        areas[cur_index] = height[cur_index] * (right_index - left_index - 1)
    return max(areas)
        
            
if __name__ == '__main__':
    map_list = [[1,0,1,1,1,1],[1,1,1,1,1,1],[1,1,1,0,1,0]]
    print(get_max_area(map_list))
    






























