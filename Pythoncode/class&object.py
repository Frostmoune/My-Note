class myclass(object):
    # 定义一个类,即class 类名(父类名),如果没有父类,则继承自object
    def __init__(self,name="Bill",score=100):
        self.name=name
        self.score=score
    # 相当于constructor,self在这里相当于this指针
    def print(self):
        print("%s %d"%(self.name,self.score))
    # 相当于class里面的一个method

newclass=myclass("Sam")
# 定义一个对象
newclass.print()
# 调用print函数
newclass.grade=6
# 给示例(newclass)绑定一个grade属性
print(newclass.grade)

newclassb=myclass()
# print(newclassb.grade)这条语句会报错
# 注意grade这个属性是newclass特有的

class Human(object):
    __grade=5
    sex="female"
    # 定义一个类属性,所有类和其实例都可以访问到
    def __init__(self,name="Sam",age=18,score=100):
        self.__name=name
        self.__age=age
        # 注意,定义是变量名前面有两条下划线的变量是类外部不可访问的,相当于private
        self.score=score
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def getgrade(self):
        return self.__grade
    def print():
        print(__name,__age)
    def __test(self):
        pass
    # 注意,这样定义的函数相当于private函数
    
newhuman=Human("Bill",19,98)
print(newhuman.score)
# print(newhuman.__name)
# print(newhuman.__age) 这两条语句都会报错,因为__name和__age变成private变量
print(newhuman.getname())
print(newhuman.getage())
# 提供一个接口才可以访问private变量
newhuman.setname("Emma")
# 提供一个接口才可以改变private变量
print(newhuman.getname())
# newhuman.print()这条语句会报错,因为形参中的self是必不可少的
newhumanb=Human()
newhumanb.__name="Simon"
print(newhumanb.__name)
print(newhumanb.getname())
# 这两条语句的输出不同,说明从外部定义的__name和类内部的__name并不是同一个变量,应当避免这样的错误
# 在Python中,变量名类似__xxx__的,也就是以双下划线开头,并且以双下划线结尾的,是特殊变量,
# 特殊变量是可以直接访问的,不是private变量,所以,不能用__name__、__score__这样的变量名.
print(newhumanb._Human__name)
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Class__name,所以，仍然可以通过_Class__name来访问__name变量,
# 但最好不要这样做
print(newhuman.sex)
print(newhumanb.sex)
# 实例可以访问到类属性sex
print(newhumanb.getgrade())
# 通过接口也可以访问到private的类属性
newhumanb.sex="male"
# 实例属性优先级高于类属性
print(newhumanb.sex)
print(Human.sex)
# 但是仍可以通过类名.属性来访问
del newhumanb.sex
# 删除实例属性
print(newhumanb.sex)
# 之后newhumanb.sex就返回类属性
del Human.sex
# 删除类属性

# print(newhuman.sex)
# print(newhuman.sex)报错,说明此后就没有sex类属性了
Human.sex="male"
# 恢复类属性
print(newhuman.sex)
# 注意只有在类内定义的__属性才是private的
# newhuman.__test()会报错,说明private的函数也不可以在外部被访问