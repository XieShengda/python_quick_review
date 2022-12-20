# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:17:06 2019

@author: XieShengda
"""

### [函数式编程]
#函数是面向过程的设计, 函数式编程是一种抽象程度很高的编程范式
'''
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''
#函数是变量
f = abs
print(f(-1))
#可以将其他值赋值给函数变量
#abs = 10 #再次以执行abs(-1)会报错类型错误

### 高阶函数(函数中传入另一个函数作为参数)
def f2(a, b, f):
   return f(a), f(b) 
print(f2(-1, 2, f))

##map/reduce
### map
l = [1,2,3]
def filter_custom(x):
    if x > 2:
        return None
    else:
        return x
print(list(map(filter_custom, l)))
print(map(filter_custom, l))
it = map(filter_custom, l)
from collections.abc import Iterator
while isinstance(it, Iterator):
    try:
        print(next(it))
    except StopIteration:
        break
print(list(map(str, l)))
g = (a + b for a in [1,2,3] for b in [4,5,6])
it = map(lambda x: x * x, g)
print('map with iterator text', next(it)) #map和reduce第二个参数可以时iterator
### reduce - 积累运算, 用法和map一样, 但是传入的函数需要有两个参数
def add(x, y):
    return x + y
from functools import reduce
print(reduce(add, [1,2,3,4]))

#组合使用
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2num(s1):
    def fn(x, y):
        return x * 10 + y
    def char2num(s2):
        return DIGITS[s2]
    print(reduce(fn, map(char2num, s1)))
    
str2num('1345')
#使用lambda简化
def str2num_simple(s): #作用等同int()
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))    
print(str2num_simple('1994'))
### filter
#全体素数序列
def odd(): #奇数队列
    n = 1
    while True:
        n += 2
        yield n

def primes():
    yield 2
    it = odd()
    while True:
        n = next(it)
        yield n
        #将奇数从小到大取素数
        it = filter(lambda x: x % n > 0, it)
x = 10
print('primes:')
for n in primes(): #生成器函数返回Iterator需要调用, 而不是函数对象
    if x == 0:
        break
    x = x - 1
    print(n)
### sorted reverse反向排序
it = sorted([2,2,1,3,0], key= lambda a: a * a, reverse = True)
for i in it:
    print(i)

### 返回函数(闭包Closure)
#执行闭包函数之前如果修改闭包中的变量, 会影响执行时的结果
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count() #count()循环返回三个函数变量
#因为执行循环时i的值变化, 所以下面三个函数结果都是9
#因为python中字面值也是对象, 闭包中保存的是引用, 引用指向的对象被更改了
print(f1())#9
print(f2())#9
print(f3())#9
#!返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # 调用函数每次会新建引用j, 每个j是不同的引用, i迭代是每次指向另一个对象地址,
        #所以每个j指向的地址不同
    return fs
f1, f2, f3 = count()    
print(f1())#1
print(f2())#4
print(f3())#9
    
### 匿名函数 lambda表达式可以没有参数, 只能有一个表达式

### 装饰器 Decorator
import functools

def log(text):
    def decorator(func):
        functools.wraps(func)#在定义增强函数之前, 隐式调用
        def wrapper(*args, **kw):
            #开始功能增强
            print('tips: ', text)
            print('call %s():' % func.__name__)
            #返回原函数的结果
            return func(*args, **kw)
        return wrapper #第一层返回函数对象
    return decorator #第二层返回函数对象
#使用装饰器
@log('提示文字')
def now():
    print('1994-10-28')
    
now()

print(now.__name__)#wrapper
##偏函数 固定参数值, 简化函数调用
int_custom = functools.partial(int, base=2)
print(int_custom('01001'))
#创建偏函数实际可以接受函数对象, *args, **kw这三个参数
max_custom = functools.partial(max, 9)
print(max_custom(1, 2, 4))# 实际传入的参数(9, 1, 2, 4), 默认参数插入到最左边


    