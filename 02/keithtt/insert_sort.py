#!/usr/local/bin/python3
#
nums=[5,13,19,21,37,56,64,75,80,88,92]

for i in range(1,len(nums)):
	for j in range(i,0,-1):
		if nums[j] < nums[j-1]:
			nums[j-1],nums[j] = nums[j],nums[j-1]

print(nums)
