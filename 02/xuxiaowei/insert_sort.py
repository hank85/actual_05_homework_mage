#!/user/bin/python3.5
#encoding: utf-8
#插入排序

nums=[6, 11, 7, 9, 4, 2, 1]

for count in range(len(nums)):
    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
            nums[index],nums[index + 1] = nums[index + 1],nums[index]

print(nums)

