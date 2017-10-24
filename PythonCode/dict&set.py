mydict={'hello':50,'world':40,'python':30,'c++':20}
print(mydict)
# 定义一个dict(注意是大括号),第一个是key,第二个是相对应的value,注意key只可以删除不可以改变
print(mydict['world'])
# 输出key对应的value
mydict['world']=90
print(mydict['world'])
# 改变key对应的value
print('c++' in mydict)
print('javascript' in mydict)
# 判断某个key是否在dict里面
print(mydict.get('c++',5))
print(mydict.get('javascript',6))
print(mydict.get('javascript'))
# 判断某个key是否在dict里面,如果在则返回对应的value,否则返回第二个参数,如果没有,
# 第二个参数则返回None
mydict['javacript']=60
print(mydict)
# 往dict里面插入一个新的key,注意dict没有append函数
mydict.pop('c++')
print(mydict)
# 往dict里面删除相应的key,pop必须有形参
# mydict[['hello','world']]=12 这条语句会报错
# dict里面的key必须是不可变的,由于list是可变的，所以不能作为key
mydict[('hello','world')]=12
print(mydict)
# 同理,tuple可以作为key来使用
myset=set([1,1,2,2,3,3,4,4])
print(myset)
# 定义一个set,即为集合
myset.add(5)
myset.add(5)
print(myset)
# 往set中加入一个新元素,重复添加没有意义
myset.remove(4)
print(myset)
# myset.remove(4)
# 从set删除相应元素,重复删除会报错
myseta=set(['Hello','world',2,3,4])
mysetb=set(['Hello','Python',23,35,4])
print(myseta|mysetb)
# 输出并集
print(myseta&mysetb)
# 输出交集