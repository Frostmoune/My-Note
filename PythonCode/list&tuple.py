mylist=['Hello','World','python']
#定义一个list,其元素是可变的
print(mylist[0])
print(mylist[-1])
# python的list,类似c++的Array
# print(mylist[3])
# 如果越界会报indexerror错误
print(mylist)
# 打印整个数组
mylist.append(32)
print(mylist)
# 在list末尾增加元素
mylist[2]='c++'
print(mylist)
# 更改元素
mylist.pop()
print(mylist)
# 在末尾pop
mylist.append('python')
mylist.pop(2)
print(mylist)
# pop指定下标的元素
mylist.append(['Hello','javascript'])
print(mylist)
# list的内部元素也可以是list
print(mylist[3])
print(mylist[3][0])
# 类似于二维数组
print(len(mylist))
# 返回list的长度
L=[]
print(len(L))
# 定义一个空list
mytuple=('a','hello world',32)
# mytuple[0]='b' 这条语句会报错
# 定义一个tuple,其初始化后内部元素不可以改变
print(mytuple)
mynewtuple=()
# 定义一个空mytuple
print(len(mynewtuple))
mytuplea=('hello world')
print(mytuplea)
mytupleb=(1)
print(mytupleb)
mytuplec=(1,)
print(mytuplec)
mytupled=('hello world',)
print(mytupled)
# 第三和第四条语句才是定义只有一个元素的tuple的方法
myliste=[1,3,4,6,2,5]
mylistf=myliste.sort()
print(mylistf)
print(myliste)
# 对list里面的元素进行排序,改变原来的list,不返回新的list,注意tuple没有sort函数