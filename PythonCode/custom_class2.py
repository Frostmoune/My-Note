class Fib(object):
    def __init__(self):
        self.a=1
        self.b=1
    def __iter__(self):
        return self # 返回self本身
        # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000000:
            raise StopIteration() # 定义迭代出口,raise表示若引发该异常,后面的代码将不会执行
        return self.a# 返回下一个值,此方法用于迭代时的next
    def __getitem__(self,n):
        if isinstance(n,int):# 判断n是不是整型
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):# 判断n是不是切片,如果是切片,n.start返回开始的下标,n.stop返回结束的下标
            a,b=1,1
            L=[]
            step=1 if n.step==None else n.step #记录切片的start、stop和step
            if step>0:
                start=0 if n.start==None else n.start if n.start>0 else 100+n.start
                stop=100 if n.stop==None else n.stop if n.stop>0 else 100+n.stop
                # 初始化切片的真实start和真实stop
                if start>=stop:
                    return L
                val=step
                for x in range(stop):
                    if x>=start:# 当下标大于start时要开始
                        if val>=step:# 计算当val==步长时才需要放进list里
                            L.append(a)
                            val=1
                        else:
                            val+=1
                    a,b=b,a+b
                return L
            if step<0:
                start=100 if n.start==None else n.start if n.start>0 else 100+n.start
                stop=0 if n.stop==None else n.stop if n.stop>0 else 100+n.stop
                if start<=stop:
                    return L
                val=-step
                for x in range(start):
                    if x>=stop:# 当下标大于stop时要开始
                        if val>=-step:
                            L.append(a)
                            val=1
                        else:
                            val+=1
                    a,b=b,a+b
                return L
            else:
                return L
        return TypeError("n should be int or slice")
        # __getitem__方法使得类的对象可以实现像list一样的下标索引和切片

from collections import Iterable,Iterator
myobj=Fib()
print(next(myobj))
print(next(myobj))
print(next(myobj))
for x in myobj:
    print(x)
print(isinstance(myobj,Iterable))
print(isinstance(myobj,Iterator))
# 说明定义了__iter__和__next__方法的类的实例是可以迭代的
print(myobj[6])
print(myobj[3:6])
print(myobj[90::2])
print(myobj[:10:1])
print(myobj[4:20:3])
print(myobj[:90:-1])
print(myobj[10::-1])
# 符合切片功能

class MyFib(Fib):
    def __init__(self):
        super(MyFib,self).__init__()
    
newobj=MyFib()
print(next(newobj))
for x in newobj:
    print(x)
print(isinstance(newobj,Iterable))
print(isinstance(newobj,Iterator))
# 说明子类可以继承父类的__iter__和__next__
print(newobj[6])
print(newobj[3:6])
print(newobj[90::2])
print(newobj[:10:1])
print(newobj[4:20:3])
print(newobj[:90:-1])
print(newobj[10::-1])
# 说明子类可以继承父类的__getitem__