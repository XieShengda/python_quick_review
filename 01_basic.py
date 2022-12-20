# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### [python基础]

### 运算符
#power(**)
a = 5
pow = a ** 0.5
print(pow)

#输入输出
# name = input("please enter your name\n")
# print("Are you "+ name + '?')

# python用大写表示常量, python中没有机制能保证变量不变, 大写只是一种习惯用法

###字符编码
x = b'abc'
print(x)
y = '中文'
z = y.encode('utf-8')

print(y.encode('utf-8'))
print(z.decode('utf-16'))
z = z.decode('utf-16')
print(len(y))
print(z.encode('utf-8'))
z= z.encode('utf-8')
print(z.decode('utf-8'))

### 字符串格式化
print('hello %2s , hello %1s ' % ('world', 'sender')) #hello world , hello sender 
print('hello {1}, {0:.1f}'.format(1.934, 'sender'))

### list
classmates = ['sender', 'xie', 'sheng', 'da']
print(classmates[2]) 
print(classmates[-1]) #最后一个
print(classmates[-2]) #倒数第二格, 不能越界

#增
classmates.append('me')
classmates.insert(1, 'he')
print(classmates)
# 删
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
multiItemList = [1, 1.1, 'a', [1, '1']] #list中的元素可以不同类型

### tuple元组
tp = ('1', 2, 3, [1, 2]) #tp中的普通元素不能修改, 但是对象可以修改, tuple中存储的是对象地址
tp[-1].append(3)
print(tp)
tp = (1) #单个元素定义成这样是整型1
tp = (1,) #定义单个元素的正确方式
tp = () #定义空tuple
print(tp)
print(bool(tp))

### 条件判断
age = 2
if age >= 18:
    print('your age is: ', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
a = None
if a: #a为非零非空则为true
    print('true')
else:
    print('false')
    print(a)
    
### 循环
l1 = [1, '1', 2, 3, 4, [4.5, 5]]
for i in l1: #迭代
    print(i)
#计算1-100的和
l2 = range(1,101)
sum = 0
for i in l2:
    sum += i

print('1-100的和是: ',sum)

#带index的for循环
for i in range(0,len(l1)):
    pass

sum = 0
n = 100
while n > 0:
    sum += n
    n = n - 1
    
print('1-100的和是: ',sum)
# break continue

### dict
d1 = {'a': 1, 'b': 2, 'c': 3}
print(d1['a'])
d1['d'] = 4
print(d1['d']) #如果key不存在会报错
### 判断可以是是否存在
if 'd' in d1:
    print('d 在字典中')
    
print(d1.get('e')) #不存在时不会报错, 而是返回None
print(d1.get('e', 111)) #不存在时返回指定的值

if 1 in l1:
    print('1在list中')
    
#删除
d1.pop('a')
print(d1)
#dict和list相比时空间换时间
#dict的key必须为不可变对象, 如str, int, 不能时list等

### set
s1 = set([1,2,2]) #用list创建set, 重复元素会被过滤
s2 = {1, 2, 3}

print(s1)
print(s2)

print(s1 & s2)#交集
print(s1 | s2)#并集, 包含s1 和 s2中所有元素

s1.add('3')
s2.remove(1)
print(s1)
print(s2)
#set也无法放入可变对象, 因为无法判断两个可变对象是否相等, 这点和java不一样

### 总结
#list appand insert pop sort
#能用tuple 就尽量不要用list
#dict []增改 pop删
#set add remove 





