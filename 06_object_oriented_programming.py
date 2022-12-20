# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:53:44 2019

@author: XieShengda
"""

#Object Oriented Programming
##创建类
class Student(object): #需要继承object
    def __init__(self, name, score): #name, score是必要参数
        #self相当于this, 必须在所有成员函数参数的第一个
        self.name = name
        self.score = score
        self.__secret = 'secret'
        
    def introduce(self):
        print(self.name)
        print(self.score)
    
    def get_secret(self):
        print(self.__secret)

tom = Student('tom', 100)
tom.introduce()

#类的成员变量直接通过self添加或获取
tom.age = 10
print(tom.age)
tom.get_age = lambda :tom.age
print(tom.get_age())

##访问控制
'''
变量类型 默认public
_xxx代表私有但是可以访问(习惯上的私有)
__xxx private 解释器会将变量改名为类似 _类名__xxx 来控制访问
__xxx__特殊变量
'''
#在外部添加和private同名的变量
tom.get_secret()
tom.__secret = 'public' #添加的是另一个变量, 原先的变量已经被改为_Student__secret
tom.get_secret()
print(tom.__secret, tom._Student__secret)

##继承和多态
class Animal(object):
    def run(self):
        print('animal is running')
class Dog(Animal): #继承Animal
    pass

dog = Dog()
dog.run()#继承Animal的run

class Dog(Animal):
    def run(self):
        print('dog is running')

dog.run()#还是原来的Dog类
dog = Dog()#指向新的Dog类
dog.run()#重写run方法
print(type(dog))
#多态的意义: 开闭原则, 对扩展开放, 对修改关闭
def run_twice(animal): #注意!animal其实没有类型, python不是强类型语言
    animal.run()
    animal.run()
    
run_twice(dog)

class Mouse(object):
   def run(self):
       print('mouse is running')
run_twice(Mouse())
'''
动态类型的'鸭子类型'(看起来像鸭子, 走起路来像鸭子, 那它就可以被看做鸭子) 
对于run_twice不是必须传入Animal类型
只要是有run方法就可以
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
'''

##获取对象信息
print(type(Animal))
#判断一个对象是否是函数
import types #type工具类
print(type(run_twice) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
#判断是否是父类
print(isinstance(dog, Animal))
#获取一个对象的所有属性和方法
print(dir(dog))
print(dir('str'))
#len(obj) 会自动调用 对象的.__len__
#可以定义类的__len__方法来让改类的对象可以被len()使用
class MyDog(object):
    def __len__(self):
        print('call __len__()')
        return 0 #len()只能调用返回int类型的函数, 否则会报错
len(MyDog())
#属性, 方法操作
setattr(dog, 'a', 'a')
if hasattr(dog, 'a'):    
    print(getattr(dog, 'a'))#如果啊不存在会raise AttributeError()
print(getattr(dog, 'b', 'b'))#属性存在返回默认值
#判断方法是否存在
print(hasattr(dog, 'run'))
#hasattr等方法只有在不知道对象信息的时候才用到
#如果能直接使用对象的属性或方法就不要使用getattr等方法
'''
使用示列
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''

##类属性
class Student(object):
    name = 'student'
s = Student()
print(s.name)#类属性
s.name = 'tom'
print(s.name)#实例属性, 比类属性优先级更高, 会屏蔽掉类属性
del s.name #删除实例属性



