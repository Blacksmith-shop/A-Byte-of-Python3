# _*_ coding:utf-8 _*_
# Author:Blacksmith 

'''这里，我们定义了一个称为 printMax 的函数，这个函数需要两个形参，叫
做 a 和 b 。我们使用 if..else 语句找出两者之中较大的一个数，并且打印较大的那个
数。在第一个 printMax 使用中，我们直接把数，即实参，提供给函数。在第二个使用
中，我们使用变量调用函数。printMax(x,y) 使实参 x 的值赋给形参 a，实参 y 的值赋
给形参 b 。在两次调用中， printMax 函数的工作完全相同。'''

def printMAX(a,b):
    if a > b:
        print(a, '是最大的')
    elif a == b:
        print(a, '等于',b)
    else:
        print(b, '是最大的')
printMAX(3,4)
x = 9
y = 10
printMAX(x,y)