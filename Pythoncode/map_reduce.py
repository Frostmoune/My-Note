def mypower(x):
    return x**3

mylist=[1,2,3,4,5,6,7,8,9]

for n in map(mypower,mylist):
    print(n)

# map()函数接收两个参数,一个是函数,一个是Iterable,map将传入的函数依次作用到序列的每个元素,并把结果作为新的Iterator返回
reslist=list(map(mypower,mylist))
# 得到迭代器构成的list
print(reslist)

mystr="HELLO WORLD"

print(list(map(str.lower,mystr)))
# 将字符串里面的元素变成小写字母

from functools import reduce
# 引入reduce
def tonum(x,y):
    if isinstance(y,str):
        return int(x)*10+int(y)
    return x*10+y

print(reduce(tonum,mylist,100))
# reduce接受三个形参,第一个形参是函数,第二个形参是序列(可迭代),第三个形参是计算的初识值
print(reduce(tonum,'12345678',10))
# 将字符串转换为数字

def strtonum(x,y):
    return x*10+y

def toint(x):
    return int(x)

print(reduce(strtonum,map(toint,'123456789')))
# 结合map的写法
print(reduce(lambda x,y:x*10+y,map(toint,'123456')))
# 用lambda表达式的写法