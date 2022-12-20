#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, threading

""" @asyncio.coroutine
def hello():
    print(threading.currentThread())
    print('hello')
    r = yield from asyncio.sleep(1) #sleep()是一个coroutine, 执行后相当于hello().send()
    print('bye')
@asyncio.coroutine
def hello_2():
    print(threading.currentThread())
    print('hello2')
    r = yield from asyncio.sleep(1) #sleep()是一个coroutine, 执行后相当于hello().send()
    print('bye2') 
loop = asyncio.get_event_loop()
tasks = [hello(), hello_2()]
loop.run_until_complete(hello()) #执行一个coroutine
loop.run_until_complete(asyncio.wait(tasks))#执行一个任务列表

loop.close() #需要关闭 """


async def hello():
    print(threading.currentThread())
    print('hello')
    r = await asyncio.sleep(1) #sleep()是一个coroutine, 执行后相当于hello().send()
    print('bye')

async def hello_2():
    print(threading.currentThread())
    print('hello2')
    r = await asyncio.sleep(1) #sleep()是一个coroutine, 执行后相当于hello().send()
    print('bye2') 
loop = asyncio.get_event_loop()
tasks = [hello(), hello_2()]
loop.run_until_complete(hello()) #执行一个coroutine
loop.run_until_complete(asyncio.wait(tasks))#执行一个任务列表

loop.close() #需要关闭
    