#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##ORM框架
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int(11)')
#model
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs): #执行类定义的时候python interpreter会调用__new__, 并将类定义中的属性及继承的基类等作为参数传入
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items(): #获取类的属性
            if isinstance(v, Field):
                print('found mapping: %s => %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)    
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)#调用dict的构造函数
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Model has no attribute "%s"' % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
        
#test
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

user = User(id='10000', username='sender', email='xieshengda@gmail.com', password='19941028')
user.save()

#exercise
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs) #返回类对象
        print('found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('found mapping: %s => %s' % (k, v))
                mappings[k] = v
                # attrs.pop(k)不能在迭代集合的时候改变集合的大小
        for k in mappings.keys():
            attrs.pop(k)
        #通过操作attrs来增减成员
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)#调用父类的构造方法
    def save(self):
        columns = []
        params = []
        args = self.values()
        for k in self.__mappings__.keys():
            columns.append(k)
            params.append('?')
        
        print('sql: insert into %s (%s) values (%s)' % (self.__table__, ','.join(columns), ','.join(params)))
        print('args: [%s]' % ','.join(args))
            
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

user = User(id='10000', username='sender', email='xieshengda@gmail.com', password='19941028')
user.save()                
                