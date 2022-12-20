# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:34:56 2019

@author: XieShengda
"""

#面向对象高级编程
class Person(object):
    pass

p = Person()
p.name = 'tom'
'给实例绑定方法'
#1
def set_age(self, age):
    self.age = age
p.set_age = set_age
p.set_age(p, 11)#需要传入对象自身
print(p.age)
#2
def set_gender(self, gender):
    self.gender = gender
from types import MethodType
p.set_gender = MethodType(set_gender, p)
p.set_gender('M')
print(p.gender)

#但是这种绑定方法对其他Person的实例无效
p2 = Person()
#p2.set_gender('F'), 会报 'Person' object has no attribute 'set_gender'

#需要给类绑定方法
Person.set_gender = set_gender
p2.set_gender('F')
print(p2.gender)
#通常setter, getter会定义在类中

'__slots__ 限定可以绑定的属性'
class Student(object):
    __slots__ = ('name', 'age') #使用tuple定义循序绑定的属性名称

s = Student()
# s.gender = 'M' 回报 no attribute 'gender'
s.name = 'sender'

#__slots__只对当前类作用, 对子类无效
class Monitor(Student):
    pass

m = Monitor()
m.gender = 'M'
# 子类中定义__slots__
class Monitor(Student):
    __slots__ = ('height')
m.age = 11
# 定义了__slots__之后子类中可以定义的属性包含父类中__slots__定义的和自己定义的
print(m.age)

##@property
class Student(object):
    @property
    def score(self):
        return self._score
    
    @score.setter #直接操作属性, 不用setter方法, 但是可以执行数据校验
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数值有误')
        self._score = value
        
    @property #没有setter 该属性为只读属性
    def is_passing(self):
        if self._score == None:
            raise ValueError('请设置分数')
        if self._score > 60:
            return True
        else:
            return False

student = Student()
student.score = 99 #实际转化为.set_score(99)
print(student.score) #实际转化为.get_score()
print(student.is_passing)
# student.is_passing = False 会报AttributeError

##多重继承
class Monitor(Person, Student):
    pass
        
##定制类
#python 版toString()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self): #print时调用
        return 'Student object(name: %s)' % self.name
    __repr__ = __str__ #直接在命令行而不用print输出时调用

print(Student('sender'))
#__iter__, __next__ 可迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self #实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a #返回下一个值
    #不可切片版本: 
    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for i in range(n):
    #         a, b = b, a + b
    #     return a
    
    #切片版本
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for i in range(n):
                a, b = b, a + b           
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            l = []
            for i in range(stop):
                if i >= start:
                    l.append(a)
                a, b = b, a + b
            return l
        else:
            raise TypeError('type error')

    def __getattr__(self, attr):
        if attr == 'max':
            return 100000 #返回属性值
        if attr == 'is_fib':
            return lambda :True #返回函数    
        # 定义了__getattr__之后如果没有下面的语句, 任何调用都会至少返回None 
        # 因为__getattr__默认返回None
        raise AttributeError(' no this attr %s' % attr) 
fib = Fib()
print(next(fib)) #自动调用next, 和 __len__一样
#__getitem__ 获取指定index的值
print(fib[3],' ', range(3)[-1])#range(3)等于range(0, 3)等于[0, 1, 2]
print(fib[10: 20]) 

#__getattr_ 当属性不存在时会调用
print(fib.max)
print(fib.is_fib()) #调用未定义的函数
# print(fib.min) #此时会报错
# 实现链式调用
class Chain(object):
    def __init__(self, path=''): #初始化, path默认为空字符串
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path)) #path 被不断更新
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().usr.share.nginx.html)

#__call__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, last_name): #可以让实例变成一个函数对象, 在运行期间动态创建, 可以添加参数
        return 'my name is %s, my last name is %s' % (self.name, last_name)
print(Student('sender')('xie'))
print(callable(Student('sender')))#判断对象是否可以被调用
print(callable(abs))#判断对象是否可以被调用

##枚举类enum
from enum import Enum, unique
Month = Enum('月', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan) #'月.Jan'
#枚举
for m in Month.__members__.items():
    print(m) #('Dec', <月.Dec: 12>)
for name, member in Month.__members__.items():
    print(name, '=>', member, ', ', member.value) #Dec => 月.Dec ,  12
#以Enum作为超类来派生类
@unique #确保没有重复值, 对象名的查重不用加也会判断
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#调用方式        
print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday(0))

##元类metaclass 类似java Class, 类类型
class Hello(object): #定义的是object类的子类, 创建出的是对象
    def hello(self, name='world'):
        print('hello, %s' % name)

print(type(Hello)) #type函数可以查看一个类型或变量的类型, 也可以创造新的类型
#python class的定义是运行时动态创建, 创建class的方法是使用type函数
Hello = type('HelloNew', (object,), dict(hello=Hello.hello))
print(type(Hello())) #<class '__main__.HelloNew'>

#metaclass 的定义(类的类型), 用来创建type
#先定义meteclass, 可以创建class, 最后创建instance
class ListMetaclass(type): #需要从type类型派生, 定义的类是type的子类, 创建的是类
    def __new__(cls, name, bases, attrs): #类对象, 类名, 类继承的超类集合, 类的方法dict
        attrs['add'] = lambda self, value: self.append(value) #添加方法add
        return type.__new__(cls, name, bases, attrs)        
class MyList(list, metaclass=ListMetaclass): #MyList通过ListMetalist创建, 有了add 函数, add也可以在类中直接定义
    pass
L = MyList()
L.add('a')
print(L) 

### 定制类总结
"""
__init__ => ClassName() //构造函数
__slots__ (tuple obj) //定义允许被添加的成员
__getattr__, __setattr__ => .运算符
__next__ => next()
__iter__ => iter() //返回一个generator
__getitem__ => [,,] slice
__call__ => func() //对象变成函数对象
__str__, __repr__
__new__(cls, name, bases, attrs) //元类构造函数, type.__new__(...) 创建类对象
"""