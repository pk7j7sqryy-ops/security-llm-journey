"""
@Author:sunqiyu
@Time:2026/6/24
@Desc:这个是文档注释，代码说明------
"""
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]
输出: [0]
'''

#方法1
# nums = [0]
# for i in nums:
#     if i == 0:
#         nums.remove(i)
#         nums.append(i)
# print(nums)

#方法2

'''
最后，在栈的末尾添加两个 0，即为答案 [1,3,12,0,0]。
为了做到 O(1) 空间复杂度，直接把 nums 当作栈，用一个变量 stackSize 表示栈的大小，初始值为 0。
入栈就是把 nums[stackSize] 置为 nums[i]，然后把 stackSize 加一。
最后把 nums 中的下标从 stackSize 到 n−1 的数都置为 0。
'''
# nums = [0,1,0,3,12]
# # nums[1:]=[0]*3
# # print(nums)
# stacksize=0
# for i in nums:
#     if i != 0:
#         nums[stacksize]=i
#         stacksize+=1
# nums[stacksize:]=[0]*(len(nums)-stacksize)
# print(nums)

#方法3

nums = [0,1,0,3,12]
# nums[1:]=[0]*3
# print(nums)
i0=0
for i in range(len(nums)):
    if nums[i]:
        nums[i], nums[i0]= nums[i0],nums[i]
        i0+=1
print(nums)
