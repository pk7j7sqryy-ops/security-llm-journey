"""
@Author:sunqiyu
@Time:2026/6/22
@Desc:这个是文档注释，代码说明------
"""
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
'''
nums = [3,2,4]#输出：[0,1]
target = 6
hashdict={}
for key,value in enumerate(nums):
    tag_num=target-value
    if tag_num in hashdict:
        print(hashdict[tag_num],key)
    hashdict[value]=key

# hashdict2={7:-1,2:1}
# print(-1 in hashdict2)

#错误方法
# nums2=[target-i for i in nums]
# print(nums2)
# nums3={i:nums.index(i) for i in nums2 if i in nums}
# print(nums3)
