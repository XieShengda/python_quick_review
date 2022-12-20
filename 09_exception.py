#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##异常处理
try:
    print('try...')
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

#except 可以有多个, 但是只会有一种异常被捕获, 子类的异常也会被捕获
try:
    r = 10/0
except BaseException as e:
    print('baseException')
except ZeroDivisionError as e: #将永远不会被捕获, 因为一定被父类baseException的捕获语句捕获
    print('zeroDivisionError')

#异常可以跨函数传递, 可以在上层函数捕获下层函数的异常
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
#如果异常一直没有被捕获会被python interpreter捕获, 并打印调用链信息, 但是程序会中断
#记录日志
import logging

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e) #可以打印日志, 通过配置还可以将日志记录到文件
main()
print('end')

#手动抛出异常
class FooError(ValueError):
    pass
def foo():
    raise FooError('foo error')

def main():
    try:
        foo()
    except FooError as e:
        logging.exception(e)
        raise #在except体内会将当前捕获到的异常原样抛出
try:
    main()
except Exception:
    print('捕获到原样抛出的异常')

##调试
#断言assert
def foo(i):
    assert i != 0, 'i is zero' # 会抛出错误
    i = 10/i
# foo(0)
# python -O filename.py 可以关闭断言

#logging(需要先import)
logging.warning('warning')
logging.info('info')
logging.basicConfig(level=logging.INFO)
#logging_level: debug info warning error

##pdb
""" 
python -m pdb filename.py
l 查看代码
n 单步执行
p 变量名 查看变量
q 结束调试

import pdb
pdb.set_trace()通过代码设置断点
python filename.py #程序会自动在段点暂停并进入pdb调试环境
"""

#使用IDE的调试功能

##单元测试
import unittest
class Test(unittest.TestCase):
    value = 1 
"""
类属性
可以通过
Test.value
或 self.value 
或 实例名.value
访问

但是只能通过Test.value = xxx修改
如果实例名.value/self.value = xxx会给实例添加属性
并且访问时优先级比类属性高
"""
    def test_init(self):
        self.assertEqual(self.value, 1) #访问到类属性
    def test_add(self):
        self.value += 1
        self.assertEqual(self.value, 2)#访问到实例属性
    def test_valueerror(self):
        with self.assertRaises(ZeroDivisionError): #期望会抛出指定错误, 抛出错误时ok
            r = 10/0
    #aop方法
    def setUp(self):#测试方法调用前执行
        print('start...')
    def tearDown(self):#测试方法调回之后执行
        print('end...')
#运行单元测试 
# 1:
""" 
if __name__ == '__main__':
    unittest.main()

$ python filename.py
"""
# 2:
"""
$ python -m unittest filename.py 
"""

