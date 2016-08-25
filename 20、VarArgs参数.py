# _*_ coding:utf-8 _*_
# Author:Blacksmith

'''要做的：在还未讨论列表和字典之前，我在后面的章节应该写这些吗？
有时，你或许想定义一个能获取任意个数参数的函数，这可通过使用 * 号来实现。'''

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))

'''当我们定义一个带星的参数，像 *param 时，从那一点后所有的参数被收集为一
个叫做 ’param’ 的列表。（译者注：如在该例中，首先会给 initial 的值由 5 变成 10 ，
然后 numbers 将 1,2,3，收集作为一个列表 numbers=(1,2,3)）。
类似地，当我们定义一个带两个星的参数，像 **param 时，从那一点开始的
所有的关键字参数会被收集为一个叫做 ’param’ 的字典。（译者注：在该例子中，
从 vegetables=50 后的所有参数收集为一个字典 keywords=’vegetables’: 50, ’fruits’:
100）。
'''

