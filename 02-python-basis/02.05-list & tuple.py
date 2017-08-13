#!usr/bin/env python
#-*- coding: utf-8-*-

#生成列表 list是一个 有序 序列，其中的元素用 , 隔开，列表元素不需要是同一类型,甚至可以包含列表,同时列表的长度也不固定
lst_1 = []
lst_2 = list()
lst_3 = range(5)  #函数生成列表,[0,1,2,3,4]

'''列表操作'''
#查看列表长度
len(lst)  

#加法和乘法
lst_1 = [1,2,'hello']
lst_2 = [2,4,'world']
print lst_1 + lst_2  #输出[1，2，'hello',2,4'world'],返回 新列表，原列表不变
print lst * 2        #输出[1,2,'hello'，1,2,'hello'],返回 新列表，原列表不变

#索引和切片
lst_3 = [1,2,3,4,5]
print lst_3[2]     #索引从0开始,输出3
print lst_3[-1]    #反向索引，输出5
print lst_3[1:4]   #切片，输出[2,3,4],返回 新列表，原列表不
print lst_3[1:-1]  #切片，输出[2,3,4],返回 新列表，原列表不变

#利用索引和切片修改list
lst_3[0] = 0
print lst_3   #输出[0,2,3,4,5],修改 原列表
lst_3[1:3] = [9,10]
print lst_3   #输出[0,9,10,4,5],修改 原列表
lst_3[3:] = [11,12,13]
print lst_3   #输出[0,9,10,11,12,13],修改 原列表,python list使用整段替换，不需要元素相等

#删除元素
lst_4 = [1,2,3,4,5]
del lst_4[0]
print lst_4  ##输出[2,3,4,5],修改 原列表

#使用关键字 in 测试从属关系
lst_5 = [1,2,3,4,5]
print 1 in lst_5   #输出True
print 10 in lst_5  #输出Flase

'''列表方法'''
  '''不改变原列表的方法'''
lst_6 = [0,1,3,4,5,2,3,4,3]
#lst.count(e) 返回列表中元素 e 出现的次数，如果 e 不在 lst 中则返回0
print lst_6.count(3)  #输出 3
#lst.index(e) 返回列表中元素 e 第一次出现的索引位置，如果 e 不在 lst 中会报错
print lst_6.index(3)  #输出2
#不存在的元素会报错
print lst_6.index(12) '''Traceback (most recent call last):
                             File "G:/Python_xiao/PyCode/ProTest/Test/demo.py", line 23, in <module>
                                print lst_6.index(12) 
                          ValueError: 30 is not in list'''
  '''改变列表的方法'''
#lst.append(e)将元素 e 添加到列表 lst 的最后，append()每次只添加一个元素
lst_6.append(9)
print lst_6   #输出[0,1,3,4,5,2,3,4,3,9]
#lst.extend(lst2)将序列 lst2 的元素依次添加到列表 lst 的最后，作用相当于 lst += lst2
lst_6.extend([10,11,12])
print lst_6   #输出[0,1,3,4,5,2,3,4,3,9,10,11,12]

#lst.insert(idx, e) 在索引 idx 处插入 e ，之后的元素依次后移
lst_6.insert(0, 99)
print lst_6     #在索引0处插入99，输出[99,0,1,3,4,5,2,3,4,3,9,10,11,12]
#lst.remove(e) 会将列表中第一个出现的 e 删除，如果 e 不在 lst 则报错
lst_6.remove(3) #移除第一个 3 ，返回[99,0,1,4,5,2,3,4,3,9,10,11,12]
#lst.pop(idx) 会将索引 idx 处的元素删除，并返回这个元素
lst_6.pop(0)    #返回 99 
#lst.sort() 会将列表中的元素按照一定的规则排序
lst_7 = [1,4,3,5,9,11,10]
lst_7.sort()
print lst_7    #输出[1, 3, 4, 5, 9, 10, 11]，原列表该表
lst_8 = sorted(lst_7)
print lst_8    #输出[1, 3, 4, 5, 9, 10, 11],且原列表 lst_7 不变
#lst.reverse() 会将列表中的元素从后向前排列
lst_9 = [1, 2, 3, 4, 5, 6]
lst_9.reverse()
print lst_9   #输出[6, 5, 4, 3, 2, 1]
