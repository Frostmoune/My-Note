def judge(x):
    if(x%2):
        return True
    return False
# 定义函数的方法,用def,别忘了冒号
for x in range(20):
    print(judge(x))

def fact(num):
    if(num==1):
        return 1
    return num*fact(num-1)
# 定义递归函数
print(fact(9))

def mypower(num,val=2):
    res=1
    for x in range(val):
        res*=num
    return res

# 函数缺省值
print(mypower(9))
print(mypower(9,3))

def printf(name='you',gender='male',grade=1,home='guangzhou'):
    print("name:",name)
    print("gender:",gender)
    print("grade:",grade)
    print("home:",home)

printf()
printf('me','female',4)
printf('me',grade=2,home='shanghai')
# 给缺省值加实参的方法

def add(L=[]):
    L.append('end')
    return L

print(add([1,2,3]))
# 正常调用该函数时,得到正常的结果
print(add())
print(add())
print(add())
# 如果默认参数为可变量,而且每一次调用函数都会对参数产生改变,则默认参数会不断发生改变
# 所以默认参数必须为不变量

def mysum(*mylist):
    sum=0
    for x in mylist:
        sum+=x
    return sum
# 定义一个具有可变参数的函数,在形参前面加*,传进去的参数会默认转换为元组
print(mysum(1))
print(mysum(1,5,3))

L=[1,5,3,4,6]
print(mysum(*L))
T=(1,5,3,4,6)
print(mysum(*T))
# 如果要将list或者tuple作为实参,则在传入参数前面加*

def enroll(name,gender,**other):
    print("name:",name)
    print("gender:",gender)
    print("other:",other)

# other是一个可变关键字参数,此时other默认转换为dict
enroll('Bill','male')
enroll('Bill','male',city='Guangzhou')
enroll('Bill','male',city='Guangzhou',grade=2)
# 往关键字参数传参数的方法

mydict={'city':'Guangzhou','grade':2,'class':6}
enroll('Bill','Male',**mydict)
# 将dict传入关键字参数的方法

def newenroll(name,gender,*,city="Guangzhou",grade):
    print(name,gender,city,grade)

# 定义具有命名关键字参数的函数,*后面的参数就是命名关键词
newenroll('Bill','Male',grade=2)
# 只接受*后面的关键字作为参数
# newenroll('Bill','Male',grade=2,myclass=6)会报错

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
# 此处'a'和'b'传入参数*args
f1(1, 2, 3, 'a', 'b', x=99)
# 此处'a'和'b'传入参数*args,x=99传入参数kw
f2(1, 2, d=99, ext=None)
# 此处d传入参数d,ext传入参数kw
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'} 
f1(*args, **kw)
# 此处1,2,3传入参数a,b,c;4传入参数args;kw传入kw
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# 此处1,2,3传入参数a,b,c;kw中的d的值传入参数d;另外的作为dict传入参数kw

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
# 组合型参数的调用