class Student(object):
    __slots__=('score','name','age','grade','className')
    # __slots__用tuple定义允许绑定的属性名称
    def __init__(self,score=60,name="",age=17):
        self.score=score
        self.name=""
        self.age=age

now=Student()
now.grade=10
now.className=5
print(now.grade)
print(now.className)
# now.sex="female"这条语句会报错,因为给对象绑定了不允许被绑定的对象属性
Student.finish="True"
print(now.finish)
# 但是绑定新的类属性是可行的