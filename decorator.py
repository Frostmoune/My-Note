def now():
    print("2017-10-09")
    return 'done'

f=now
print(f())
print(f.__name__)
print(now.__name__)
# 每个函数都有__name__属性,返回该函数的名字,注意此时函数不需要括号

def log(myfunction):
    def mycall(*mylist,**mydict):
        print('Call:%s():'% myfunction.__name__)
        # 打印函数名字
        return myfunction(*mylist,**mydict)
        # 执行并返回函数
    return mycall
    # 返回一个函数
# 定义一个decorator

def sum():
    print("2017-10-09")
    return 'done'
sum=log(sum)
print(sum())
print(sum.__name__)
# 打印出的名字为mycall

@log
def sum():
    print("2017-10-09")
    return 'done'
print(sum())
# 上面两块语句是等价的
# decorator的定义语法便是
# @decorator
# def func()

def mylog(text):
    def mydecorator(func):
        def wrapper(*args,**kw):
            print("Hello %s %s"%(text,func.__name__))
            func(*args,**kw)
            print('Goodbye %s %s'%(text,func.__name__))
            return 'done'
        return wrapper
    return mydecorator
# 三层嵌套(带参数的)decorator

@mylog('Hello')
def world(*args,**kw):
    print("Hello World!")
# 这条语句相当于 world=mylog('Hello')(world)
# 上面这条语句首先执行mylog('Hello'),它返回一个decorator,之后就相当于world=mydecorator(world)
world()

def mylog(func):
    def wrapper():
        print('Hello %s'%func.__name__)
        func()
        print('Goodbye %s'%func.__name__)
    return wrapper

@mylog
def Bill():
    print("I'm Bill")

Bill()
print(Bill.__name__)
# 注意,经过decorator修饰的函数,其__name__已经变成了decorator内部的函数,如此时Bill()的__name__已经变成了wrapper
# 因为最终返回的函数是wrapper,其名字是wrapper
import functools
# 要解决这种情况,需要引入functools
def mylogb(func):
    @functools.wraps(func)
    # 这条语句用于将func的__name__等属性复制到wrapper函数中
    def wrapper():
        print('Hello %s'%func.__name__)
        func()
        print('Goodbye %s'%func.__name__)
    return wrapper

@mylogb
def Bill():
    print("I'm Bill")

Bill()
print(Bill.__name__)
# 此时名字则没有改变,而带参数的decorator也可用相同方法