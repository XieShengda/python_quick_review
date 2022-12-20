# -*- coding: utf-8 -*-

##文件读写
try:
    """ 
    'r' 读
    'w' 写(覆盖)
    'a' 写(append)(不会覆盖)
    'rb' 读二进制, 图片视频等
    encoding='xxx' 读取非utf-8编码文件
    errors='ignore' 忽略UnicodeDecodeError
    """
    f = open('d://test.txt', 'r')#文件不存在会报IOError
    if f.read() == '':
        print('文件为空')
finally:
    if f: #f is not None    
        f.close()

#with-as
with open('d://test.txt', 'r') as f:
    print(f.read())

with open('d://test.txt', 'w') as f:
    f.write('谢胜达\n第二行')
#read
with open('d://test.txt', 'r') as f:
    print('read(size): ', f.read(128))#按字节数读取
    #如果后面再调用则不会读到数据, 因为test.txt文件流已经被读取完
    print('readline(): ', f.readline())#读取一行
    print('readlines(): ',f.readlines())#读取所有行, 并且返回list
with open('d://test.txt', 'r') as f:
    print(f.readline())
    print(f.readlines())#只能读取到第二行

##StringIO, BytesIO 在内存中读写str和bytes(对获取到的数据进行操作并且不写入硬盘)
from io import StringIO, BytesIO
print('\n StringIO =>')
f = StringIO()
f.write('hello, world')
f.write('\n')
f.write('i am sender')
print(f.getvalue())

f = StringIO('init\nthis is the second method')
"""
```要使得下面语句起作用, StringIO()构造函数不应该被传入参数
f.write('\nit is new')
print(f.getvalue()) #只能获得无参StringIO() write的值
"""
#read只能读取到StringIO()传入参数的值
# print(f.read())

while True:
    s = f.readline()
    if s == '':
        break
    # print(type(s))
    print(s.strip()) #删除头尾空格

# for s in f.readlines(): #换行符会导致多余的空行
#     print(s)

print('\nBytesIO =>')
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO('长一点的中文'.encode('utf-8'))
print(f.read()) #不是str所以不用readline()
"""
总结: write => getvalue, 传参 => read
"""

##操作文件和目录
#操作系统名
import os, shutil
# os.uname() 操作系统名详情在windows上不提供
#环境变量
print(os.name, '\n', os.environ)
print(os.environ.get('PATH'))

#当前目录
print(os.path.abspath('.'))
#创建目录
temp_dir = os.path.join(os.path.abspath('.'), 'temp')
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
    # os.rmdir(temp_dir)
os.mkdir(temp_dir)
#拆分目录
print(os.path.split(temp_dir)) #将最后一级文件或目录拆分
#创建文件
file_path = os.path.join(temp_dir, 'file.txt')
open(file_path, 'w') #如果文件不存在则新建, 需要存在目录才可以创建文件
#拆分文件扩展名
print(os.path.splitext(file_path))#拆分文件扩展名
#删除目录, 只能删除空目录
# os.rmdir(temp_dir)
shutil.rmtree(temp_dir)
#列出当前目录所有文件夹
print([d for d in os.listdir('.') if os.path.isdir(d)])#列表生成式
print([f for f in os.listdir(os.path.join('.', 'exercise')) if os.path.isfile(os.path.join(os.path.abspath(os.path.join('.','exercise')),f)) and os.path.splitext(f)[1]=='.py'])
# for f in os.listdir('./exercise'):
#     print(f)

##序列化
import pickle
d = dict(name='sender', age='18')
db = pickle.dumps(d) #将返回对对象的bytes
print(db)
print(pickle.loads(db))

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f) #序列化之后写入文件
with open('dump.txt', 'rb') as f:
    d = pickle.load(f) #反序列化
print(d)

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'I am a student, my name is %s and my age is %d years old' % (self.name, self.age)
print(pickle.dumps(Student('sender', 18)))
#JSON
import json
# print(json.dumps(Student('sender', 18)))#会报错, json只能dumps(dict)
j = json.dumps(Student('sender', 18), default=lambda obj: obj.__dict__)#__dict__变量存储对象属性
print(j)
print(json.loads(j)) #反序列化
def dict2student(d):
    return Student(d['name'], d['age'])
print(json.loads(j, object_hook=dict2student))#object_hook dict转成对象的函数
obj = dict(name='小明', age=20)
#确保ascii属性默认为True, 会将中文转义为unicode, False则原样输出
s = json.dumps(obj, ensure_ascii=False)
print(s)
s = json.dumps(obj)
print(s)
s = json.dumps(obj, ensure_ascii=True)
print(s)

