g=(x*x for x in range(0,10) if x%2==0)
# 把列表生成式的中括号改成小括号,即得到一个生成器
print(next(g))
print(next(g))
print(next(g))
# 生成器会一个一个返回下一个元素,若超出范围会抛出异常
for x in g:
    print(x)
# 遍历生成器的所有元素

def test():
    L=[]
    for i in range(0,10):
        if len(L)==0:
            L.append(1)
        else:
            tempL=[L[j]+L[j+1] for j in range(0,len(L)-1)]
            L=[]
            L.append(1)
            L.extend(tempL)
            # 这条语句将一整个list拼接到另一个list的末尾
            L.append(1)
        yield L
    return L
# 这是一个generator函数,在每次调用next()的时候执行,遇到yield语句返回,再次执行时从上次返回的yield语句处继续执行。

for n in test():
    print(n)
# 返回得到一个杨辉三角

from collections import Iterable
print(isinstance(test(),Iterable))
# 说明生成器是一个可迭代对象
L=[1,2,3,4,5]
mydict={'1':'x','2':'y','3':'z'}
from collections import Iterator
print(isinstance(L,Iterator))
print(isinstance(mydict,Iterator))
print(isinstance(test(),Iterator))
# 说明list、dict等数据类型都不是iterator,这些数据类型都没有next操作

print(isinstance(iter(L),Iterator))
print(isinstance(iter(mydict),Iterator))
# 这样就能将list、dict等数据类型转换为iterator

a=iter(L)
b=iter(mydict)
c=iter(mydict.items())
print(next(a))
print(next(a))
print(next(b))
print(next(b))
print(next(c))
print(next(c))
# 转换为迭代器后就有了next操作