#/bin/env python
#encoding:utf-8

import random

#插入排序法
# 算法描述：
#     1.从第一个元素开始，该元素可以认为已经被排序
#     2.取出下一个元素，在已经排序的元素序列中从后向前扫描
#     3.如果该元素（已排序）大于新元素，将该元素移到下一位置
#     4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
#     5.将新元素插入到该位置后
#     6.重复步骤2~5

#生成一个随机数组
n=0
random_list = []
while n <8:
	num  =  random.randint(0,100)
	if num not in random_list:
		random_list.append(num)
		n += 1

print(random_list)
insert_num = int(input('以上是一个随机的列表，请输入要出入列表的数据进行排序：'))
input_list = [insert_num] + random_list

for i in range(1,len(input_list)):
	key = input_list[i]
	for j in range(i-1,-1,-1):
		if input_list[j] > key:
			input_list[j+1] = input_list[j]
		else:
			break
		input_list[j] = key


print('插入排序结果：')
print(input_list)

#二分查找法
# [一维数组，折半查找]
# 假如有一组数为3，12，24，36，55，68，75，88要查给定的值24.可设三个变量front，mid，end分别指向数据的上界，中间和下界，mid=（front+end）/2.
# 1.开始令front=0（指向3），end=7（指向88），则mid=3（指向36）。因为mid>x，故应在前半段中查找。
# 2.令新的end=mid-1=2，而front=0不变，则新的mid=1。此时x>mid，故确定应在后半段中查找。
# 3.令新的front=mid+1=2，而end=2不变，则新的mid=2，此时a[mid]=x，查找成功。
# 如果要查找的数不是数列中的数，例如x=25，当第三次判断时，x>a[mid]，按以上规律，令front=mid+1，即front=3，出现front>end的情况，表示查找不成功。

print('二分法从以上列表查找数据。')
search_num = int(input('请输入要查找的数字：'))
front = 0
end = len(input_list) - 1
while True:
	if front > end:
		print('找不到，输入的数字不在列表里！')
		break
	mid = int((front + end) / 2)
	if input_list[mid] > search_num:
		end = mid -1
	elif input_list[mid] < search_num:
		front = mid + 1
	elif input_list[mid] ==  search_num:
		print('要查找的数字找到了，在列表的index是：',input_list.index(search_num))
		break