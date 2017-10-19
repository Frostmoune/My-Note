import math
# 表示引入math包

def myfact(num):
    if not isinstance(num,int):
        return TypeError("wrong type")
# isinstance用于检查传进去的参数类型是否正确,若不正确,则返回一个错误类型
    if num==1:
        return 1
    return num*myfact(num-1)

print(myfact(6))
print(myfact('6'))
print(myfact(6.66))

def equation(a,b,c):
    if (not isinstance(a,(int,float))) or (not isinstance(b,(int,float))) or (not isinstance(c,(int,float))):
        return TypeError("Wrong Type!")
    delta=math.sqrt(pow(b,2)-4*a*c)
    if a==-1:
        first='-'
    elif abs(a)!=1:
        first=str(a)
    if a!=1:
        res=first+'x^2'
    else:
        res='x^2'
    if b>0:
        res+='+'+str(b)+'x'
    else:
        res+=str(b)+'x'
    if(c>0):
        res+='+'+str(c)
    else:
        res+=str(c)
    return res,(-b+delta)/(2*a),(-b-delta)/(2*a)
# 返回值有多个的情况,用逗号将返回值之间隔开,最后返回一个tuple

print(equation(1,-3,2))
print(equation(-6,5,3))


