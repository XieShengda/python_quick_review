# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:13:11 2019

@author: XieShengda
"""

### [函数 abstraction抽象]

### 函数调用
#内置函数
print(abs(-11))
print(max(1,2,3))
print(str(1.2))

#函数名是一个指向函数的引用 函数作为对象和js相似
a = abs
print(a(-1))

### 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-9))

#定义空函数
def nop():
    pass#什么也不执行, 作用是可以用作占位符, 在没有想好怎么写之前可以用, 让代码不报错

### 类型检查

a = 'a'
if not isinstance(a, (int, str)):
    raise TypeError('type error')
    
### 多个返回值
def multi_return():
    return 1, 2
print(multi_return()) #返回一个tuple

#没有return自动return None

#参数
### 位置参数default
def power(x, n = 2):#默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))

def enroll(name, gender, age = 6, city = 'Beijing'):
    print(name)
    print(gender)
    print(age)
    print(city)
enroll('sender', 'M', city = 'Hangzhou')
#默认参数必须指向不变对象, 默认参数实际是一个对象
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
add_end()
print(add_end()) #['END', 'END', 'END', 'END']
#修正上面的函数
def add_end_fix(L=None):
    if L == None: #或者L is None
        L = []
    L.append('END')
    return L
print(add_end_fix())
print(add_end_fix([1,2,3]))
### 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    return sum
#调用可变参数函数
print(calc(1,2,3))
#传入tuple/list
nums = [1,2,3]
print(calc(*nums))
### 关键字参数
def person(name, city, **kw):
    print('name', name, 'city', city, 'kw', kw)
person('sender', 'Hangzhou')
person('sender', 'Hangzhou', job = 'Engineer', gender = 'M')#kw被解析成dict
extra = { 'job': 'Engineer', 'gender': 'M'}
person('sender', 'Hangzhou', **extra)
#总结 *是转为tuple, **是转为dict
#命名关键字参数, 必须传入命名关键字参数, 否则不会报错
def person_rename(name, city, *, job, gender):
    print(name, city, job, gender)
#如果已经有可变参数, 可以省略*
def person_rename_2(name, city, *args, job, gender):
    print(name, city, args, job, gender)
person_rename('sender', 'Hangzhou', job = 'Engneer', gender = 'M')
person_rename_2('sender', 'Hangzhou', 'args', job = 'Engineer', gender = 'job')
### 参数组合
def person_rename_3(name, city, *args, job, **kw):
    print(name, city, args, job, kw)
#调用参数组合1
person_rename_3('sender', 'Hangzhou', 'xie', 'sheng', 'da', job = 'Engineer', gender = 'M')    
#调用参数组合2
zh_name = ['xie', 'sheng', 'da']
info = {'gender': 'M', 'qq': '7932'}
person_rename_3('sender', 'Hangzhou', *zh_name, job = 'Enginner', **info)
### 递归函数
#计算阶乘1*2*..*n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(10))
'''
使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
''' 

    
    
    