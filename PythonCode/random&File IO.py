import random

print(random.random())
# 生成一个0-1的随机浮点数
print(random.uniform(-20,50))
# random.uniform(a,b)用于生成一个a~b的浮点数
print(random.randint(-20,50))
# random.uniform(a,b)用于生成一个a~b的整数
print(random.randrange(-20,50,3))
# 在range(-20,50)中得到步长为3的序列,生成这个序列中的随机数
mylist=["Hello","World","C++","Javascript","Java","C","HTML","CSS","Python","Android"]
print(random.choice(mylist))
# 在一个序列(string、tuple、list等)随机选一个元素
random.shuffle(mylist)
print(mylist)
# 将原有序列随机打乱,返回被打乱的序列
# mytuple=("Hello","World","C++","Javascript","Java","C","HTML","CSS","Python","Android")
# random.shuffle(mytuple)
# 不可用于tuple
newlist=["Android Studio","Visual Studio","eclipse","Matlab","Vivado","Dev"]
newslice=random.sample(newlist,3)
# 返回一个序列的随机切片
print(newslice)
print(newlist)
# 不会改变原有的序列

ifile=open("test.txt",'w')
# 以写方式打开文件
for x in range(0,20):
    n=random.randint(2,21)
    ifile.write("%d\n"%n)
    # 将数据或字符写入文件
    for y in range(0,n):
        num=random.randint(-500,500)
        ifile.write("%d "%num)
    ifile.write("\n")

ifile.write("-1\n")
ifile.close()

with open("test.txt") as ofile:
    print(ofile.read())
# read一次性读取文件的全部内容,第二个参数默认为‘r’,即默认为读操作

# 这一条语句相当于try:
#     ofile = open('/path/to/file', 'r')
#     print(ofile.read())
# finally:
#     if ofile:
#         ofile.close()
# 是为了避免产生IOerror

ofile=open("test.txt",'r')

array=[]
for line in ofile.readlines():
    # readlines用于一行一行的处理文件数据
    array=[]
    mystr=str(line).strip()
    if mystr=="-1":
        break
    if mystr.isdigit():
        continue
    j=0
    for i in range(0,len(mystr)):
        if(mystr[i]==' '):
            array.append(int(mystr[j:i]))
            j=i+1
    array.append(int(mystr[j:len(mystr)]))
    print(array)
# 这一部分用于将之前生成的测试数据读取到一个数组中
ofile.close()
