print(abs(-2))
# 返回绝对值
print(max(1,2))
print(min(1,3,4,7,8,9))
# max(min)返回最大(最小)值,并能接受多个参数
mylist=[1,3,7,8,9,2,5]
print(max(mylist))
mytuple=(3,9,3,7,6,5)
print(min(mytuple))
# 同理可以接受list和tuple做形参,但list的tuple内部的元素必须定义过大小关系
# mytuple=(3,9,3,7,6,5,'a') print(min(mytuple))会报错
print(int(123.345))
print(float(5))
print(str(-3.1452))
print(bool(1.25))
print(bool(0.00))
print(bool('abc'))
print(bool(''))
print(bool(1))
print(bool(0))
# 数据类型转换函数,bool只有为空或者为0是返回false