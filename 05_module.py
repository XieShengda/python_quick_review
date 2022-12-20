#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:00:13 2019

@author: XieShengda
"""

#Module
#第一行#!/usr/bin/env python3注释可以让这个py文件直接在Unix/Linux/Mac上运行
#第二行# -*- coding: utf-8 -*- 表示py文件本身使用标准utf-8编码
#在python中一个py文件是一个module, 模块避免变量名和函数名冲突
#package 避免模块名冲突
'''
自己创建模块时要注意命名，
不能和Python自带的模块名称冲突。
例如，系统自带了sys模块，自己的模块就不可命名为sys.py，
否则将无法导入系统自带的sys模块。
'''
#使用模块
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many arguments')

#在命令行执行时 if判断才会成立, 可以在命令行运行时执行额外代码, 最常见的是测试
if __name__=='__main__':
    test()

#安装第三方模块
'''
方法1: 包管理工具pip, pip3 install xxx/ pip install xxx
方法2: Anaconda，
这是一个基于Python的数据处理和科学计算平台，
它已经内置了许多非常有用的第三方库，我们装上Anaconda，
就相当于把数十个第三方模块自动安装好了，非常简单易用。
'''
import numpy
print(numpy.abs(-1))
#print(sys.path)
for p in sys.path:
    print(p)
    
#添加模块搜索路径, 路径内的模块可以被import, 配置环境变量PYTHONPATH
    