def newclosure(*mylist):
    def sumforeven():
        sum=0
        for x in mylist:
            if x%2==0:
                sum+=x
        return sum
    return sumforeven
# 函数内部有函数,返回值是一个函数,这样就定义了一个closure(闭包)

f=newclosure(*range(0,101))
# 注意传参数时的*号
print(f)
# 打印f的类型
print(f())
# 执行f

from functools import reduce

def nextclosure(*mylist):
    def mysum():
        return reduce(lambda x,y:x+y,mylist)
    return mysum
# 另一种写求和的方法

fa=nextclosure(*range(0,20))
fb=nextclosure(*range(0,20))
print(fa)
print(fb)
# 注意两次定义的函数是不同的函数
print(fa==fb)
print(fa()==fb())
# 但返回值是相同的

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行,因此i的当前值被传入f()
    return fs
# 写闭包时要注意,返回函数不要引用任何循环变量,或者后续会发生变化的变量。

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

def mycount():
    def f(j):
        return lambda: j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

# 用lambda表达式简化过的代码
f1,f2,f3=mycount()
print(f1(),f2(),f3())

