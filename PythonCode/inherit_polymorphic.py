class Animal(object):
    __name="Animal"
    start="test"
    def __init__(self,number=0,nowtype="Animal",info="private"):
        self.type=nowtype
        self.number=number
        self.__info=info
    def run(self):
        print("There're %d %ss runing"%(self.number,self.type)) #会根据调用该函数的具体子类决定输出内容
    def __call(self):
        print("Call %d %ss"%(self.number,self.type)) #同上
    def getname(self):
        print(Animal.__name)
    def call(self): # 私有函数__call()的接口
        self.__call()
        print(self.__info)

class Dog(Animal): #Dog继承Animal
    def __init__(self,number=0,nowtype="Dog",color="white"):
        # self.Animal(number,nowtype)
        super(Dog,self).__init__(number,nowtype) # 上一条语句是错的,super(class名,对象名)返回对应class的父类
        # 这样才能调用父类构造函数
        # 如果子类定义了自己的初始化函数,而没有显示调用父类的初始化函数,则父类的属性不会被初始化
        self.color=color
    def run(self):
        print("Call Dog.run()")
        super(Dog,self).run() #调用父类同名函数,需要采用super方法返回父类
        print(self.start) #子类可以访问父类的非私有类属性
        self.getname() #子类可以直接调用父类非同名函数
    def call(self):
        # self.__call() 
        # super(Dog,self).__call() 这两条语句都是错误的,说明子类不能直接调用父类的私有函数
        super(Dog,self).call()
        # print(self.__info)
        # print(super(Dog,self).__info) 这两条语句都是错误的,说明子类不能直接访问父类的私有变量

class Cat(Animal): #Cat继承Animal
    def __init__(self,number=0,nowtype="Cat",color="black"):
        super(Cat,self).__init__(number,nowtype)
        self.color=color
    def run(self):
        print("Call Cat.run()")
        super(Cat,self).run()
        print(self.start)
        self.getname()
    def call(self):
        # self.__call()
        # super(Cat,self).__call()
        super(Cat,self).call()
        # print(self.__info)
        # print(super(Cat,self).__info)

class HelloKitty(Cat): #HelloKitty继承Cat
    def __init__(self,name="HelloKitty"):
        super(HelloKitty,self).__init__()
        self.name=name #定义子类属性
    def getname(self):
        print(self.color,self.name) #子类可以直接访问父类的非私有变量

def runs(nowobject):
    nowobject.run()
    # 传入newobject会解析所对应的类,会调用对应的类的函数,若无则往父类中找

def call(nowobject):
    nowobject.call()

zoos=[Animal(1),Dog(2),Cat(3),HelloKitty()]

for x in zoos:
    runs(x)
    call(x)
    print("\n")

print(isinstance(zoos[0],Animal)) #True
print(isinstance(zoos[0],Dog)) #False
print(isinstance(zoos[1],Animal)) #True
print(isinstance(zoos[1],Dog)) #True
print(isinstance(zoos[3],Animal)) #True
print(isinstance(zoos[3],Cat)) #True
print(isinstance(zoos[3],HelloKitty)) #True
print(isinstance(zoos[3],Dog)) #False
# 当isinstance的第二个参数是第一个参数(对象)的类名或者父类名时,返回True

print(type(zoos[0]))
print(type(zoos[1])==type(Animal)) #False
print(type(zoos[1]))
print(type(zoos[3])==type(Animal)) #False
print(type(zoos[3])==type(Cat)) #False
print(type(zoos[3]))
# 注意,type只能返回对象直接对应的类型,不等于其父类的类型

        