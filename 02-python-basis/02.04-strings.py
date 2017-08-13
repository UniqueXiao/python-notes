#!usr/bin/env python
#-*-coding: utf-8-*-

#生成字符串使用单引号或双引号，但不可混用
str1 = 'hello world'
str2 = "hello world"

'''简单操作'''
#加法
str3 = str1 + str2
str4 = 'hello' + 'world'
#乘法
print 'echo' * 3    #输出 "echoechoecho"
#字符串长度
print len(str4)  #输出12

'''字符串方法'''
#分割 str.split(sep)以给定的sep为分隔符对str进行分割,并以 列表 的形式返回分割得到的所有字符串
line = '1 2 3 4 5'
print line.split(' ') #输出'1', '2', '3', '4', '5']

#连接 str.join(str_sequence)以str为 连接符 将字符串序列str_sequence中的元素连接起来，并返回连接后得到的 新字符串,原字符串不变
str_1 = ','
str_2 = 'world'
print str_1.join(str_2)  #输出'w,o,r,l,d'

#替换 str.replace(part1, part2)将字符串str中指定的部分part1替换成想要的部分part2，并返回 新字符串,原字符串不变
str_3 = 'hello world'
print str_3.replace('world', 'Uniquexiao') #输出'hello Uniquexiao'

#大小写转换 str.upper()方法返回一个将s中的字母全部大写的 新字符串;  str.lower()方法返回一个将s中的字母全部小写的 新字符串,原字符串不变
print 'hello world'.upper() #输出'HELLO WORLD'
print 'HELLO WORLD'.lower() #输出'hello world'

#去除多余空格
str_4 = '  hello world  '
str_4.strip()  #str.strip()返回一个将str两端的多余空格除去的 新字符串,原字符串不变
str_4.lstrip()  #str.lstrip()返回一个将str开头的多余空格除去的 新字符串,原字符串不变
str_4.rstrip()  #str.rstrip()返回一个将str结尾的多余空格除去的 新字符串,原字符串不变

#更多方法  可以使用 dir（str） 函数查看所有可以使用的方法
'''
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__getslice__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_formatter_field_name_split',
 '_formatter_parser',
 'capitalize',
 'center',
 'count',
 'decode',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'index',
 'isalnum',
 'isalpha',
 'isdigit',
 'islower',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
 '''


#多行字符串 用一对 """ 或者 ''' 来生成多行字符串
str_5 = '''hello world.
it is a nice day!'''   #在储存时，我们在两行字符间加上一个换行符 '\n'  'hello world.\nit is a nice day.'

#使用 () 或者 \ 来换行  当代码太长或者为了美观起见时，我们可以使用 () 或 \ 将一行代码转为多行代码
str_6 = ('hello world.'
        'it is a nice day!')  #'hello world.it is a nice day'
str_7 = 'hello world.'\
        'it is a nice day!'   #'hello world.it is a nice day'
        
#强制转换字符串   str(object)/repr(object)强制将object转化成字符串,但需注意两者区别
print str(1.1 + 2.2)    #输出'3.3'
print repr(1.1 + 2.2)   #输出'3.3000000000000003'

#整数与不同进制的字符串转化
hex(255) #十六进制 '0xff'
oct(255) #八进制   '0377'
bin(255) #二进制   '0b11111111'

#使用int/float将字符串转换为整数/浮点数
int('23')               #默认十进制，23
int('FF', 16)           #指定16进制，255
int('377', 8)           #指定8进制，255
int('11111111', 2)      #指定2进制，255
float('3.5')            #浮点数，3.5

#格式化字符串 使用 % 或 format()方法格式化字符串，%已逐渐被淘汰，推荐使用format()
print '{} {} {}'.format('a', 'b', 'c')    #输出'a b c',字符串中花括号 {} 的部分会被format传入的参数替代，传入的值可以是字符串，也可以是数字或者别的对象
print '{0} {2} {1}'.format('a', 'b', 'c')    #可用数字指定传入参数的位置,输出'a c b'
print {color} {n} {x}'.format(n=10, x=1.5, color='blue')  #指定传入参数的名称,输出'blue 10 1.5'
print '{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color='blue')  #可以混合使用,输出'blue 10 1.5 foo'
from math import pi
print '{0:10} {1:10d} {2:10.2f}'.format('foo', 5, 2 * pi) #用{<field name>:<format>}指定格式,输出'foo                 5       6.28'
# % 格式化字符串
str = 'The price is'
num = 15.5
t = '%s %.2f' % (str, num)
print t   #输出'The price is 15.5'







