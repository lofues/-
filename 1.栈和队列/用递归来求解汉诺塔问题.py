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
def hanoiProblem(num:int, left:str ,mid:str ,right:str ,From:str ,to:str ):
    if num < 1:
        return 0
    else:
        return process(num,left,mid,right,From,to)


def process(num:int,left:str,mid:str,right:str,From:str,to:str):
    if num == 1:
        if From == 'mid' or to == 'mid':
            print('move 1 from ' + From + ' to ' + to)
            return 1
        else:
            print('move 1 from ' + From + ' to ' + 'mid')
            print('move 1 from '+'mid' + ' to ' + to)
            return 2
    if From == 'mid' or to == 'mid':
        another = 'right' if From == 'left' or to == 'left' else 'left'
        part1 = process(num-1,'left','mid','right',From,another)
        print('move ' + str(num) +' from ' + From + ' to ' + to)
        part2 = 1
        part3 = process(num-1,'left','mid','right',another,to)
        return part1 + part2 + part3
    else:
        part1 = process(num-1,'left','mid','right',From,to)
        print('move '+str(num) +' from '+From+' to ' + 'mid')
        part2 = 1
        part3 = process(num-1,'left','mid','right',to,From)
        print('move '+str(num) +' from '+' mid '+' to ' +to)
        part4 = 1
        part5 = process(num-1,'left','mid','right',From,to)
        return part1 + part2 + part3 + part4 + part5

if __name__ == '__main__':
    times = hanoiProblem(5,'left','mid','right','left','right')
    print('-------------------')
    print('It takes %d times'%(times))











