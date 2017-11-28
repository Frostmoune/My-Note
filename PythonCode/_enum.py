from enum import Enum, unique

week=Enum('week',('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))
# 定义week类型的枚举类

for x in week:
    print(x.name,x,x.value)
    # 输出member的名字 week.member名字 member的value(默认为从1开始根据member位置递增)

for name, member in week.__members__.items():
    print(name, '=>', member, '=>', member.value)
    # 另一种输出member的name和value的方法

@unique
class Year(Enum):
    Jan = 'a' 
    Feb = 'b'
    Mar = 'c'
    Apr = 'd'
    May = 'e'
    Jun = 'f'
    Jul = 'g'
    Aug = 'h'
    Sep = 'i'
    Oct = 'j'
    Nov = 'k'
    Dec = 'l'

for x in Year:
    print(x.name,x,x.value)

month=Year.Jun
print(month)
print(Year.Feb)
print(Year['Jul'])
# 几种通过member名字访问枚举类Year的member方法
print(Year.Sep.value)
print(Year['Aug'].name)
# 访问对应的value和name的方法
print(Year('b'))
# 根据value来访问枚举类Year的member
print(Year('e').name==Year.May.name)
print(Year('e').value==Year.Dec.value)
# 访问name和value的方法