print(list(filter(lambda x:x%2==0,range(0,101))))
# filter用于对数列进行筛选,第一个形参是函数,第二个形参是一个序列(可迭代),
# 根据第一个函数的返回值决定元素是被保留还是被删除

print(list(filter(lambda x:x and x.strip(),'h e l l o wo r l d')))
# strip用于移除字符串头尾指定的字符,没有实参则默认字符为空格
# 用于删除字符串中的空格

from collections import Iterator
print(isinstance(filter(lambda x:x%2!=0,range(0,10)),Iterator))
# filter返回一个generator

import math

primearr=[2]

def isprime(x):
    for num in primearr:
        if num>=math.floor(math.sqrt(x))+1:
            break
        if x%num==0:
            return False
    primearr.append(x)
    return True

print(list(filter(isprime,range(2,1001))))
# 用素数筛法生成1000以内的所有素数

print(list(filter(lambda x:x%2==0 and str(x)==str(x)[::-1],range(0,10000))))
# 得到所有是偶数的回文数

L=[148,521,269,931,256,129,393,427,215,631,841,170,301]
print(sorted(L))
# sorted即python内置的排序函数,默认为从小到大排序,排序时元素之间必须定义了<关系,不改变原来的序列
print(sorted('HelloWorld',key=str.lower))
# 按照不区分大小写的字典序排序,key是自定义的排序方式(还可以用cmp)

def mycomp(x):
    numx=x//10
    numx%=10
    return numx

print(sorted(L,key=mycomp))
# 按照十位数字进行排序
print(sorted(L,key=mycomp,reverse=True))
# 返回倒序(从大到小),reverse用于定义是否倒序,默认为false
