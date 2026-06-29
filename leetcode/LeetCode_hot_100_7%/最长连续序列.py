"""
@Author:sunqiyu
@Time:2026/6/22
@Desc:这个是文档注释，代码说明------
"""

'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''

'''
若 x-1 在集合里：说明 x 不是一段连续数字的开头，跳过
若 x-1 不在集合：x 是起点，往后不断找 x+1、x+2...，统计长度
'''
nums = [100,4,5,1,3,21]
set_test=set(nums)
max_length=0
for i in set_test:
    if i-1 not in set_test:
        step=1
        while i+1 in set_test:
            i += 1
            step += 1
            max_length+=1
        max_length=max(max_length,step)
print('长度为=',max_length)

#方式2
# nums.sort()
# print(nums)
# dict_test={}
# for i in nums:
#     if i+1 in nums:
#         dict_test[i]=i
# print('长度为=',len(dict_test)+1)