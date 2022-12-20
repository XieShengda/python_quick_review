#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer(): #执行返回generator
    r = 'init'
    while True:
        #接受生产者的产品
        n = yield r
        #如果为空, 返回
        if not n:
            return
        #不为空, 消费
        print('customing...')
        #返回消费结果
        r = '[200: ok]'
def produce(c):
    #start generator
    r = c.send(None) #第一次send从generator第一行开始执行直到yield
    print(r)# r = init
    for i in range(1, 6):
        print('producing...')
        print(c.send(i))#从 第一个yield开始执行, 并将i传入并顺序执行直到下一个yield
    #关闭consumer
    c.close()

produce(consumer())