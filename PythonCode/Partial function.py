print(int('1234567'))
# int可以将字符串转换为整数
print(int('64',base=16))
# int还可以接收base参数,将相应进制的转换为十进制的
print(int('10000101',2))

def tobinary(num,base=2):
    if isinstance(num,str):
        return int(num,base)
    return int(str(num),base)

print(tobinary(101010))
print(tobinary('01110110'))
print(tobinary(10000,10))
print(tobinary('123456',base=10))
# 一种二进制转十进制的函数及其调用方式

mydict={'base':'10'}
mylist=[8]
# print(tobinary(101010,**mydict))
# print(tobinary('123456',*mylist))
# 这两条语句会报错
import functools
# 引入partial
mybinary=functools.partial(int,base=2)
# 创建偏函数,实际上是固定了int函数的base参数,传入缺省值2

print(mybinary('1000101'))
# 与tobinary的功能相同

mymax=functools.partial(max,101)
# 这条语句给max传入一个缺省参数
print(mymax(8,19,99))
# 这条语句相当于：
# args = (101, 8, 19, 99)
# max(*args)

def mylog(text):
    def mydecorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return mydecorator

@mylog('Call')
def mymax(*mylist):
    return max(*mylist)

print(mymax([x*x for x in range(1,11) if x%2==0]))
