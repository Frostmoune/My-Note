print(ord('A'))
# 获取字符的整数表示
print(ord('中'))
# 同上
print(chr(66))
# 打印相应整数的字符
print(chr(25991))
# 同上
n='中文'.encode('utf-8')
print(n)
# encode用于确定编码类型
k=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(k)
# 根据编码类型确定字符
print(len(k))
print(len(n))
# 得到字符串的长度
print ("Hi,There\'re %d %s for %.2f\n" % (10,"hello world",3.1415926))
# 格式化字符串，格式控制符类似于c的printf,最后一个%和括号里面的就是要打印的字符
mystr="hello world"
mystrb=mystr.replace('h','H')
print(mystr)
print(mystrb)
# replace把字符串相应的元素用另一个元素代替,并返回代替后的字符串,原字符串不改变