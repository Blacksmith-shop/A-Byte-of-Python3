# _*_ coding:utf-8 _*_
# Author:Blacksmith 

'''如果想指定特定的关键参数为 keywor-only 而不是位置参数，可以在带星的参数后申明：'''

def total(initial=5, *numbers, vegetables):
    count = initial
    for number in numbers:
        count += number
    count += vegetables
    return count

print(total(10, 1, 2, 3, vegetables=50))
print(total(10, 1, 2, 3,))

'''在带星号的参数后面申明参数会导致 keyword-only 参数。如果这些参数没有默认
值，且像上面那样不给关键参数赋值，调用函数的时候会引发错误。
如果你想使用 keyword-only 参数，但又不需要带星的参数，可以简单地使用不适
用名字的空星，如 def total(initial=5, *, vegetables)。'''