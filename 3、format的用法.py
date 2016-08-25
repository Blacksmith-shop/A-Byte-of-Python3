#format语法使用
age = 25
name = "铁匠"
print('{0} 今年 {1} 岁了'.format(name, age))
print('为什么是 {0} 这个时候玩Python呢?'.format(age))


#下面代码输出的是：'Swaroop wrote A Byte of Python'
'{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python')

#填入下划线（_）与文本4中心（^）11宽度
'{0:_^11}'.format('hello')