import re

s1="01256"
s2="23abc"
s3="abc_56"
s4="aBc++Defg"

print(re.match(r'\d+',s1))
print(re.match(r'\d+',s2))
print(re.match(r'\d+',s3))
# 匹配至少由一个数字构成的字符串(\d表示数字)
print(re.match(r'\w{2,5}',s1))
print(re.match(r'\w{2,5}',s2))
print(re.match(r'\w{2,5}',s3))
# 匹配由2-5个字母或数字组成的字符串(\w表示字母或数字,{}里面的表示个数)
print(re.match(r'[A-Za-z]{2,5}',s1))
print(re.match(r'[A-Za-z]{2,5}',s2))
print(re.match(r'[A-Za-z]{2,5}',s3))
print(re.match(r'[A-Za-z]{2,5}',s4))
# 匹配由2-5个字母组成的字符串([A-Za-z]表示字母)(必须是某个字符串的开头部分)
print(re.match(r'[0-9]{2,3}[A-Za-z]{2,5}',s1))
print(re.match(r'[0-9]{2,3}[A-Za-z]{2,5}',s2))
print(re.match(r'[0-9]{2,3}[A-Za-z]{2,5}',s3))
print(re.match(r'[0-9]{2,3}[A-Za-z]{2,5}',s4))
# 匹配由2-3个数字开头后有2-5个字母的字符串
print(re.match(r'^.+[A-Za-z]{2,5}$',s1))
print(re.match(r'^.+[A-Za-z]{2,5}$',s2))
print(re.match(r'^.+[A-Za-z]{2,5}$',s3))
print(re.match(r'^.+[A-Za-z]{2,5}$',s4))
# 匹配由任意字符开头但以2-5个字母结尾的字符串(^表示以什么开头,.表示任意字符,$表示以什么结尾)
print(re.match(r'^[a|0]\w+',s1))
print(re.match(r'^[a|0]\w+',s2))
print(re.match(r'^[a|0]\w+',s3))
print(re.match(r'^[a|0]\w+',s4))
# 匹配由a或0开头,以字母或数字结尾的字符串
