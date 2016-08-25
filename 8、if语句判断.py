# _*_ coding:utf-8 _*_
# Author:Blacksmith 

number = 23     #数，答案 = 23
guess = int(input('输入一个整数：')) #猜上面的number

if guess == number:
    print('恭喜你，你猜到了 .') # 新的块从这里开始
    print('(但你没有赢得任何奖项！ )') # 新的块结束在这里
elif guess < number:
    print('不，它比那个高一点 ') # 另一块
    # 你可以在一个块中做任何你想做的事…
else:
    print('不，它比那稍微低一点 ') # 你一定猜>数量到达这里

print('已完成')   # 最后这句话总是执行,if语句后执行
