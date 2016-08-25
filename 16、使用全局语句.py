# _*_ coding:utf-8 _*_
# Author:Blacksmith 

'''global 语句被用来声明 x 是全局的 —— 因此，当我们在函数内把值赋给 x 的时
候，这个变化也反映在我们在主块中使用 x 的值的时候。
你可以使用同一个 global 语句指定多个全局变量。例如 global x, y, z 。'''
x = 50
def func():
    global x
    print('x is',x)
    x = 2
    print('Changed global x to',x)
func()
print('Value of x is',x)

'''不语：global 呢是代表全局的意思  你定义了一个函数，名字是func（）先不看global那一行
第一行是print('x is',x); 这样会报错的，因为x未定义，
如果你想用函数外面的变量 x 就需要 global 定义一下，告诉 python 我这个 x 是全局变量，可以为外部定义的值
这样 python 就认为 x 是定义的 而且等于 50  所以 print('x is',x);  就不会报错 而且 x 等于50'''