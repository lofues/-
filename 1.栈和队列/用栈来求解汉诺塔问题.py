"""
    用两种方法解决汉诺塔问题：
        1,递归   2,非递归：栈
    要求：
        移动汉诺塔的过程中，不能直接从左移动到右，要先移动到mid，从右到左同理
        打印出每一步移动的过程以及返回总步数
        如 2层汉诺塔的移动过程:
            move 1 from left to mid
            move 1 from mid to right
            move 2 from left to mid
            move 1 from right to mid
            move 1 from mid to left
            move 2 from mid to right

            move 1 from left to mid
            move 1 from mid to right

            It will take 8 steps
"""
