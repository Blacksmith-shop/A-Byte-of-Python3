# _*_ coding:utf-8 _*_
# Author:Blacksmith 

'''在函数中，我们第一次使用 x 的值的时候， Python 使用函数声明的形参的值。
接下来，我们把值 2 赋给 x 。 x 是函数的局部变量。所以，当我们在函数内改
变 x 的值的时候，在主块中定义的 x 不受影响。在最后一个 print 语句中，我们证明
了主块中的 x 的值确实没有受到影响。'''
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

'''不语：你在外面 定义了  x = 50  注意 你定义的函数 def func(x)  括号里面的 x  是形参，
形参你不用按书上说的理解那么难，他就是代替函数内部变量的东西，就是个代理商，
卖的商品还是 工厂生产的东西（x = 50 ),运行外就会被销毁，
在函数后面有个  func(x)  注意括号有个 x  就代表向函数 func 传入 x 变量的值'''