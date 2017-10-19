class Animal(object):
    def __init__(self):
        self._number=1
        print("Animal is constructed")
    def getnumber(self):
        return self._number

class Land_Animal(Animal):
    def __init__(self):
        super(Land_Animal,self).__init__()
        self._number=2
        print("Land_Animal is constructed")

class Marine_Animal(Animal):
    def __init__(self):
        super(Marine_Animal,self).__init__()
        self._number=3
        print("Marine_Animal is constructed")

class Fish(Marine_Animal):
    def __init__(self):
        super(Fish,self).__init__()
        self._number=4
        print("Fish is constructed")

class Dog(Land_Animal):
    def __init__(self):
        super(Dog,self).__init__()
        self._number=5
        print("Dog is constructed")
# 以上类的构造顺序与C++中类的构造顺序相同

class Turtle(Marine_Animal,Land_Animal):
    def __init__(self):
        super(Turtle,self).__init__()
        self._number=6
        print("Turtle is constructed")
# 这里需要注意的是,在Turtle里面,构造顺序按照继承类表的从右到左,然后共同的基类Animal只被构造了一次
# 注意python的类中并没有protected变量

# #class Turtle_1(Animal,Marine_Animal,Land_Animal):
#     def __init__(self):
#         super(Turtle_1,self).__init__()
#         print("Turtle is constructed") 
# 注意,这样的继承在python里会报错,因为Marine_Animal和Land_Animal均有共同的父类Animal

zoos=[Animal(),Land_Animal(),Marine_Animal(),Fish(),Dog(),Turtle()]

for x in zoos:
    print(x.getnumber())