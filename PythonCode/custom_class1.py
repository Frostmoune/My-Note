class Student(object):
    __slots__=('_score','__name','__age','grade','className')
    def __init__(self,name="",score=60,age=17):
        self._score=score
        self.__name=name
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            return TypeError("The age must be an integer")
        if age<0:
            return ValueError("The age must be positive")
        self.__age=age
        return "Done"
    @property
    def name(self):
        return self.__name

print(Student('Bill'))
# 打印出<__main__.Student object at 0x0345EB10>

class NewStudent(Student):
    __slots__=()
    def __init__(self,name="",score=60,age=17):
        super(NewStudent,self).__init__(name,score,age)
    def __str__(self):
        return "Hello,My name is %s.\nI'm %d years old.\nI'm from class %d grade %d"%(self.name,self.age,self.className,self.grade)
    # 为类定义好__str__()方法,当print该类的一个对象的时候会调用__str__()
    __repr__=__str__
    # 加上这条语句,在终端直接输入对象名,也能够按照自己想要的字符串输出对象
    def __call__(self,string):
        return string+str(self._score)
    # 定义__call__方法后,可以将对象作为函数来调用

who=NewStudent("Bob",80,19)
who.grade,who.className=6,5
print(who)
# 根据__str__方法打印出相应的内容
print(who("My score is "))
s=Student()
print(callable(max)) #函数可以被调用
# callable用于判断一个对象是否可以被调用
print(callable([1,2,3]))
print(callable("abcde"))# list和str类型均不可被调用
print(callable(s))# 没有定义__call__()方法的类实例不可以被调用
print(callable(who))# 定义了__call__()方法的类实例可以被调用

class MoreStudent(NewStudent):
    __slots__=()
    def __init__(self,name="",score=60,age=17):
        super(MoreStudent,self).__init__(name,score,age)

more=MoreStudent("Sam")
print(callable(more)) #True
print(more("My score is "))
# 子类可以继承父类的__call__()方法
more.grade,more.className=6,5
print(more)
# 子类同样可以继承父类的__str__()和__repr__()方法
    
