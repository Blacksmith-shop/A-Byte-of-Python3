# _*_ coding:utf-8 _*_
# Author:Blacksmith 

'''当在函数 func_inner 的内部时，在函数 func_outer 的第一行定义的 ’x’ 相对来讲
既不是在局部范围也不是在全局的作用域中，使用这样的 x 称之为非局部 x ，因此可以使用这个变量。
将非局部变量 x 变成全局变量 x ，可以通过将语句本身移除，在这两个例子中观察不同。'''

def func_outer():
    x = 2
    print('x is',x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Changed local x to',x)

func_outer()