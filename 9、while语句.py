# _*_ coding:utf-8 _*_
# Author:Blacksmith

#只要在一个条件为真的情况下， while 语句允许你重复执行一块语句。
#while 语句是所谓循环语句的一个例子。 while 语句有一个可选的 else 从句。

number = 23
running = True

while running:
    guess=int(input("输入一个整数："))

    if guess == number:
        print("恭喜你，你猜对了.")
        running = False   #这将导致在循环停止
    elif guess > number:
        print("不，这个有点高了.")
    else:
        print("不，这个有点低了.")
else:
        print("当循环结束 .")     # 做任何你想在这里做的事
print("完成")