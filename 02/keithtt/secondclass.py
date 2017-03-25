列表

1、使用中括号包含
2、每个元素之间用逗号分隔
3、可包含任意数据类型

列表是有序的数据集，通过列表名[索引]的方式访问列表中的元素

索引编号：
从左向右依次为 0，1，2，3，…，n–1
从右向左一次为 -1，-2，-3，…，-n

元素修改：
通过直接给 列表名[索引] 修改对应索引位置的值 
修改元素的索引必须存在，否则报错

类型转换：
通过函数list将其他可遍历的类型转化为列表
>>> list('abcdefg')
['a', 'b', 'c', 'd', 'e', 'f', 'g']

使用range函数快速创建列表

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for i in range(10):
... 	print(i)
... 
0
1
2
3
4
5
6
7
8
9

>>> list(range(9,4,-1))
[9, 8, 7, 6, 5]

1、找出最大的数
nums=[6, 11, 7, 9, 4, 2, 1]
i=nums[0]
for j in nums:
	if i <= j:
		i=j
print(i)	 

找出最小数
nums=[6, 11, 7, 9, 4, 2, 1]
i=nums[0]
for j in nums:
	if i >= j:
		i=j
print(i)		

2、移动nums中最大的数字到最后
- 比较len(nums-1)次
- 从左往右依次两两比较，如果前面比后面大，则交换位置：nums[i]和nums[i+1]比较
- 如何交换：
temp=a 
a=b 
b=temp

>>> a=10
>>> b=9
>>> temp=a
>>> a=b
>>> b=temp
>>> a,b
(9, 10)

nums=[6, 11, 7, 9, 4, 2, 1]
for i in range(len(nums)-1):
	if nums[i] > nums[i+1]:
		nums[i],nums[i+1] = nums[i+1],nums[i]
print(nums)		
[6, 7, 9, 4, 2, 1, 11]

冒泡排序
nums=[6, 11, 7, 9, 4, 2, 1]
for j in range(len(nums)-1):
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			nums[i],nums[i+1] = nums[i+1],nums[i]
print(nums)	
[1, 2, 4, 6, 7, 9, 11]

x,y,z=1,2,3
>>> a,b
(9, 10)
>>> a,b = b,a 
>>> a,b
(10, 9)
>>>

获取list中元素的最大值、最小值
>>> nums
[6, 11, 7, 9, 4, 2, 1]
>>> max(nums)
11
>>> min(nums)
1

判断元素是否存在于list中
>>> nums
[6, 11, 7, 9, 4, 2, 1]
>>> 7 in nums
True
>>> 5 in nums
False
>>> 5 not in nums
True

删除列表中的元素（根据索引）
>>> nums
[6, 11, 7, 9, 4, 2, 1]
>>> del nums[0]
>>> nums
[11, 7, 9, 4, 2, 1]

列表的四则运算
加(+)：必须为两个list相加
乘(*)：必须一个为整数

>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

list切片
按照规则获取list中一部分元素生成新的list

list[start:end:step]
list[::step]
list[start:end]
list[:end]
list[start:]
list[:]

>>> nums=list(range(10))
>>> nums[:5]
[0, 1, 2, 3, 4]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums[4:]
[4, 5, 6, 7, 8, 9]
>>> nums[4:7]
[4, 5, 6]
>>> nums[4:7:2]
[4, 6]	

切片的应用：

1、复制列表
>>> nums=list(range(10))
>>> nums_temp=nums[:]
>>> nums_temp[0]='keith'
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums_temp
['keith', 1, 2, 3, 4, 5, 6, 7, 8, 9]

2、反转list
>>> nums[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

获取索引为偶数的元素组成的list
>>> nums[::2]
[0, 2, 4, 6, 8]

获取索引为奇数的元素组成的list
>>> nums[1::2]
[1, 3, 5, 7, 9]

3、利用切片增删改
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
修改
>>> nums[1:4]
[1, 2, 3]
>>> nums[1:4]=['a','b','c']
>>> nums
[0, 'a', 'b', 'c', 4, 5, 6, 7, 8, 9]
删除
>>> nums[1:4]=[]
>>> nums
[0, 4, 5, 6, 7, 8, 9]
>>> nums[1:4]
[4, 5, 6]
增加
>>> nums[1:1]=['a','b','c']
>>> nums
[0, 'a', 'b', 'c', 4, 5, 6, 7, 8, 9]

list的函数

append：添加元素到list最右侧
clear：清空list中的元素
copy：复制list中的所有元素到新list中并返回
count：计算list中存在相同元素的数量
extend：将一个可遍历数据中的所有元素追加到list后
index：获取元素在list中的位置
insert：在list指定位置前添加元素
pop：弹出list中指定位置的元素（默认最右侧）
remove：移除list中指定的元素
reverse：对list中元素进行反转
sort：对list中元素进行排序


>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> help(list.append)
Help on method_descriptor:
append(...)
    L.append(object) -> None -- append object to end

>>> nums=[1,2,3]
>>> nums.append('a')
>>> nums
[1, 2, 3, 'a']
>>> nums.append('b')
>>> nums
[1, 2, 3, 'a', 'b'] 

>>> help(list.extend)
Help on method_descriptor:
extend(...)
    L.extend(iterable) -> None -- extend list by appending elements from the iterable 

>>> nums
[1, 2, 3, 'a', 'b']
>>> nums.extend('abc')
>>> nums
[1, 2, 3, 'a', 'b', 'a', 'b', 'c'] 

>>> help(list.insert)
Help on method_descriptor:
insert(...)
    L.insert(index, object) -- insert object before index

>>> nums=['a','b','c']
>>> nums.insert(1,1)
>>> nums
['a', 1, 'b', 'c'] 

>>> help(list.clear)
Help on method_descriptor:
clear(...)
    L.clear() -> None -- remove all items from L

>>> nums=list(range(10))
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.clear()
>>> nums
[]  

>>> help(list.copy)
Help on method_descriptor:
copy(...)
    L.copy() -> list -- a shallow copy of L  

>>> nums=list(range(10))
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums_cp=nums.copy()
>>> nums_cp
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

弹出（根据索引）
>>> help(list.pop)
Help on method_descriptor:
pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.pop()
9
>>> nums.pop(0)
0
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8]

删除（根据元素的值）
>>> help(list.remove)
Help on method_descriptor:
remove(...)
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> nums
[1, 2, 3, 4, 5, 6, 7, 8]
>>> nums.remove(3)
>>> nums
[1, 2, 4, 5, 6, 7, 8]

反转
>>> nums=list(range(10))
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.reverse()
>>> nums
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

排序
>>> nums=[3,8,5,9,1,4,6]
>>> nums.sort()
>>> nums
[1, 3, 4, 5, 6, 8, 9]

返回指定元素值的索引编号
>>> help(list.index)
Help on method_descriptor:
index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> nums=[3,8,5,3,9,1,4,6]
>>> nums.index(3)
0
>>> nums.index(3,nums.index(3)+1)
3

队列
先进先出
list.append+list,pop(0)

堆栈
先进后出
list.append+list.pop

1、Todolist
提示用户输入do或者任务
如果用户输入任务，则添加到list中
如果用户输入do，当任务为空时打印无任务并退出，否则根据先进先出原则从list中打印任务

tasks=[]
while True:
	input_text=input('plz input do or a task: ')
	if input_text != 'do':
		tasks.append(input_text)
	else:
		if len(tasks) == 0:
			print('无任务')
			break
		else:
			task=tasks.pop(0)
			print('任务：', task)	

2、获取两个list中相同的元素放到第三个列表中

nums_1=[1,2,3,4,5,3,10,11]
nums_2=[1,2,3,1,4,5,5,3,12,34]
result=[]
for i in nums_1:
	if i in nums_2 and i not in result:
		result.append(i)
print(result)

元祖

不可变的列表
使用小括号包含
可包含任意数据类型
不支持增删改

>>> t=(1,2,3,4,5)
>>> t[1]
2
>>> t[-1]
5

当元组只有一个元素时，元素后的逗号不能省略
>>> a=(1)
>>> b=(1,)
>>> type(a)
<class 'int'>
>>> type(b)
<class 'tuple'>

>>> c=1
>>> d=1,
>>> type(c)
<class 'int'>
>>> type(d)
<class 'tuple'>

元祖和列表可以互相转换
>>> tuple([1,2,3,4,5])
(1, 2, 3, 4, 5)
>>> list(tuple([1,2,3,4,5]))
[1, 2, 3, 4, 5]

元组是有序的数据集，通过元组名[索引]的方式访问元组中的元素

索引编号
从左向右依次为0，1，2，3，…，n–1
从右向左一次为-1，-2，-3，…，-n

访问元素的索引必须存在，否则报错

>>> nums=(1,2,3,4,5)
>>> len(nums)
5
>>> max(nums)
5
>>> min(nums)
1
>>> 1 in nums
True
>>> 8 not in nums
True

元祖的四则运算
加(+)：必须为两个tuple相加
乘(*)：必须一个为整数

>>> a=(1,2,3)
>>> b=(4,5,6)
>>> a+b
(1, 2, 3, 4, 5, 6)
>>> a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> b*3
(4, 5, 6, 4, 5, 6, 4, 5, 6)

元祖切片
按照规则获取tuple中一部分元素生成新的tuple

tuple[start:end:step]
tuple [::step]
tuple[start:end]
tuple[:end]
tuple [start:]
tuple[:]

>>> a=(1,2,3,4,5,6,7)
>>> a
(1, 2, 3, 4, 5, 6, 7)
>>> a[:3]
(1, 2, 3)
>>> a[4:7]
(5, 6, 7)
>>> a[4:7:2]
(5, 7)

元祖的不可变性

不可变指的是元组的内元素的值不可变
对于list等复杂数据类型的为引用方式存储数据类型，其地址不可变，但内部数据可变

>>> nums=(1,2,3,['a','b','c'])
>>> nums[0]='a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> nums[-1].append(1)
>>> nums
(1, 2, 3, ['a', 'b', 'c', 1])

元祖的函数

>>> help(tuple.count)
Help on method_descriptor:
count(...)
    T.count(value) -> integer -- return number of occurrences of value

>>> help(tuple.index)
Help on method_descriptor:
index(...)
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> nums=(1,2,3,['a','b','c'])
>>> nums
(1, 2, 3, ['a', 'b', 'c'])
>>> nums.count(3)
1
>>> nums.count(-2)
0

第一个2的索引位置
>>> nums.index(2)
1
>>> nums.index(-2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple

第二个2的索引位置
>>> nums=(1,2,3,4,3,2,1)
>>> nums.index(2,nums.index(2)+1)
5

str的formate函数

>>> help(str.format)
Help on method_descriptor:
format(...)
    S.format(*args, **kwargs) -> str
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

>>> name='keith'
>>> age=18
>>> print("i'm {}, and i'm {} years old.".format(name,age))
i'm keith, and i'm 18 years old. 

format可以通过索引引用

>>> print("i'm {1}, and i'm {0} years old.".format(name,age))
i'm 18, and i'm keith years old.   

format可以通过变量引用

>>> print("i'm {name}, and i'm {age} years old.".format(name='keith',age=18))
i'm keith, and i'm 18 years old.

format可以定义占位长度，并指定对齐方式

>>> print("i'm {name:10}, and i'm {age} years old.".format(name='keith',age=18))
i'm keith     , and i'm 18 years old.
左对齐（默认就是左对齐）
>>> print("i'm {name:<10}, and i'm {age} years old.".format(name='keith',age=18))
i'm keith     , and i'm 18 years old.
右对齐
>>> print("i'm {name:>10}, and i'm {age} years old.".format(name='keith',age=18))
i'm      keith, and i'm 18 years old.
居中
>>> print("i'm {name:^10}, and i'm {age} years old.".format(name='keith',age=18))
i'm   keith   , and i'm 18 years old.					