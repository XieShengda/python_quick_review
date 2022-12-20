# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:32:40 2019

@author: XieShengda
"""

### 切片Slice [start: end(不包含): step], :各部分的值都可以省略, step为负数则倒序
l1 =[1,2,'3',4]
print(l1[1: 3]) #第二, 三个元素 [2, '3']
print(l1[-1]) #最后一个元素
print(l1[-2:]) #倒数第二个到最后一个元素
print(l1[:2]) #前两个元素
print(l1[1:]) #第二个到最后一个元素
print(l1[::2]) #步长为2
print(l1[:]) #原样复制

#tuple切片
print((1,2,3)[1:2]) #第二个元素 (2,)
#字符串切片
print('xieshengda'[::2])
#实现trim函数去除字符串首尾的空格
def trim(s):
    index_s = 0
    index_e = len(s)
    for c in s:
        if c == ' ':
            index_s += 1 #python没有++操作
        else:
            break
    
    for i in range(len(s)-1, index_s-1, -1):
        if s[i] == ' ':
            index_e -= 1
        else: 
            break
    return index_s, index_e, s[index_s:index_e]
    
print(trim('   sss   '))
#优化版
def trim_opti(s):
    if len(s) != 0:    
        while s[:1] == ' ': #如果第一个元素是空格
            s = s[1:] #切掉第一个元素
        while s[-1:] == ' ': #如果最后一个元素是空格
            s = s[:-1] #切掉最后一个元素
    return s
print(trim_opti('  s1  '))
s1 = 'abcd'
print(s1[1: -1])
#迭代
#for-in
#判断是否可迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([], Iterable))
print(isinstance(123, Iterable))
### enumerate 枚举获取索引
for i, value in enumerate(['a','b','c']):
    print(i, value)
# 获取最大值和最小值
def max_and_min(l):
    max = None
    min = None
    for i in l:
        if max is None:
            max = i
        else:
            if max < i:
                max = i
        if min is None:
            min = i
        else:
            if min > i:
                min = i
    return max, min
print(max_and_min([1, 3, 4, 8, -1]))

#range总结
print(type(range(10, -1, -1)))
print(type([1,2]))
for i in range(10, -1, -1): #和slice一样, 包含第一个数, 不包含第二个数
    print(i)
    
### 列表生成式 iterable
print([x * y for x in range(1, 11) for y in [1,3,5]]) #全排列
print([x ** 2 for x in range(1, 11)])

#迭代dict
d = {'a':1, 'b':2, 'c':3}
print([k + ':' + str(v) + ' ' for k, v in d.items()]) #python中不能跨类型+

### 生成器generator
#把列表生成式的[]换乘()就是generator, iterator
#generator保存的是算法, 不会讲列表的所有元素都加载
g = (x for x in range(10)) #g是一个生成算法
print(next(g))#获取下一个元素
# 通过for循环获取
for n in g:
    print(n)
# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, ' ')
        a, b = b, a + b           
        n += 1
    return 'done'
print('fib:')
fib(10)
'''
a, b = b, a + b           
不断把坐标向右移动
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
但是不必写出临时变量t
''' 
### generator函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:#需要给循环添加退出条件, 否则就会创造一个无限数列出来
        yield b #遇到yield就返回, 再次调用next(g)时从yield后面开始执行
        a, b = b, a + b           
        n += 1
f = fib(10)
print(next(f))
print(next(f))
#也可以使用for循环
#获取返回值 next(g)是内建函数
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print('return ', e.value)
        break

### 迭代器 generator是迭代器对象
from collections.abc import Iterator
print(isinstance((a for a in range(10,0,-1)), Iterator))
# ()中使用, 分隔, []中使用: 分隔
# Iterable 转为 Iterator iter('abc')
# python调用内建函数一般是将对象放括号里, 而java一般是采用继承, 用点调用
# Iterator表示的是一个数据流, 计算是惰性的, 可以表示无限大的数, list等需要提前知道大小
#python 的for循环是通过不断调用next(*)实现的
l = [1,2,3]
for i in l:
    print(i)
#等价于:
it = iter(l)
while True:
    try:
        print(next(it))
    except StopIteration: #as e
        break
 
    
    
    
    
    
    
    
    
    
    