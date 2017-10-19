sum=0
mylist=[1,2,3,4,5,6,7,8,9,10]
for x in mylist:
    if(x%2):
            sum+=x
    else:
            print(x)
print(sum)
# for循环与判断,注意缩进以及循环和判断语句后面的冒号
sum=0
for x in range(5):
    sum+=x
print(sum)
# range(5)生成0~4的整数序列
print(list(range(5)))
# list把range(5)变成list类型
sum=0
for i in range(5):
    sum+=mylist[i]
print(sum)
# 另一种for循环
sum=0
n=10
while n>0:
    sum+=n
    n-=1
print(sum)
# while循环,注意不支持--和++运算符
        
