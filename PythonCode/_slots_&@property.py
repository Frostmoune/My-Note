class Student(object):
    __slots__=('_score','__name','__age','grade','className')
    # __slots__用tuple定义允许绑定的属性名称
    def __init__(self,name="",score=60,age=17):
        self._score=score
        self.__name=name
        self.__age=age
    @property
    # python内置的decorator,可以将一个方法变成属性来调用
    def age(self):
        return self.__age
    @age.setter
    # property本身又创建了一个叫age.setter的新decorator,
    # 负责将一个setter方法变成属性赋值
    def age(self,age):
        if not isinstance(age,int):
            return TypeError("The age must be an integer")
        if age<0:
            return ValueError("The age must be positive")
        self.__age=age
        return "Done"
    @property
    def score(self):
        return self._score
    # 此时没有定义score.setter方法,表明score是一个只读的方法属性


now=Student()
now.grade=10
now.className=5
print(now.grade)
print(now.className)
# now.sex="female"这条语句会报错,因为给对象绑定了不允许被绑定的对象属性
Student.finish="True"
print(now.finish)
# 但是可以绑定新的类属性
print(now.age)
# 调用def age(self),即age的getter函数
now.age=19
# 调用def age(self,age),即age的getter函数
print(now.age)
print(now.score)
# 由于score是一个只读属性,now.score=70这条语句会报错

class NewStudent(Student):
    def __init__(self,name="",score=60,age=17):
        super(NewStudent,self).__init__(name,score,age)

who=NewStudent("Bill")
who.sex="female"
print(who.sex)
# 注意如果子类没有定义__slots__属性,则父类的__slots__对于派生的子类的对象无限制
# 注意外部定义__slots__,如NewStudent.__slots__=('finish'),并没有效果

class OldStudent(Student):
    __slots__=('finish')
    def __init__(self,name="",score=60,age=17):
        super(OldStudent,self).__init__(name,score,age)

whos=OldStudent("Bob")
# whos.sex="male" 会报错,原因是如果子类定义了__slots__属性,
# 那么子类的__slots__就是子类本身定义的__slots__加上父类的__slots__
print(whos.age)
whos.age=20
print(whos.age)
# 子类可以继承父类定义的property