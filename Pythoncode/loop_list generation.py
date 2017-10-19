L=['hello','world','python','c++','javascript','x86','mips','verilog','matlab','css','html']
print(L[0:3])
# 返回L的0到3元素组成的list
print(L[:3])
# 返回L的0到3元素组成的list
print(L[2:])
# 返回L的2到末尾的元素组成的list
print(L[-2:])
# 返回L的倒数第二号元素到末尾组成的list
print(L[-2:-1])
# 返回L的倒数第二号元素到倒数第一号元素组成的list
print(L[::2])
# 返回所有元素,每两个取一个组成的list
print(L[1:9:3])
# 返回1到9号元素,每三个取一个组成的list
print(L[::-1])
# 返回反转后的list
# tuple和字符串也有同样的操作,返回的结果是tuple(字符串)

from collections import Iterable
# 从collections模块引入Iterable类型
print(isinstance('abc',Iterable))
print(isinstance(L,Iterable))
print(isinstance(5,Iterable))
# Iterable用于判断是否可以迭代
for i,j in enumerate(L):
    print(i,j)
# emuerate函数用于将一个list变成索引-元素对
for x in ([(1,2,9),(1,3,5),(1,4,7),(2,5,8)]):
    print(x)
# 这条语句输出一个又一个tuple
for x,y,z in ([(1,2,9),(1,3,5),(1,4,7),(2,5,8)]):
    print(x,y,z)
# 这条语句把tuple拆分成元素一行一行输出

import math
def isprime(num):
    flag=0
    if num==1:
        flag=1
    for x in range(2,math.floor(math.sqrt(num))+1):
        if num%x==0:
            flag=1
            break
    return True if flag==0 else False

lista=[x*x for x in range(1,10)]
print(lista)
# 打印生成1到10的数的平方组成的list
listb=[x for x in range(1,100) if isprime(x)]
print(listb)
# 生成1到100之间的质数组成的list
listc=[x*x for x in range(1,100) if isprime(x)]
print(listc)
# 生成1到100之间的质数的平方组成的list,x*x是要生成的数,x是迭代,isprime(x)是条件
listd=[(m,n) for m in range(1,10) if m%2==0 for n in range(100,110) if n%2!=0]
print(listd)
# 两重循环,生成全排列.这条语句就是生成1到10的所有偶数和100到110的所有奇数的全排列

mydict={}
level=65
for x in range(0,26):
    mydict[x+1]=chr(level+x)

for x in mydict:
    print(x)

for x in mydict.keys():
    print(x)
# 默认输出的只是dict的key

for x in mydict.values():
    print(x)
# 只输出dict的value

for x,y in mydict.items():
    print(x,y)
# 输出dict的key和value






