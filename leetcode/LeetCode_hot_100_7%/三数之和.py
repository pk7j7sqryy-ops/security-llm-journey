"""
@Author:sunqiyu
@Time:2026/6/26
@Desc:这个是文档注释，代码说明------三数之和
"""

'''
给你一个整数数组 nums，找出所有和为 0 且不重复的三元组 
[nums[i], nums[j], nums[k]]。要求满足 i != j、i != k 且 j != k，
并且 nums[i] + nums[j] + nums[k] == 0。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
'''
#方式1
list1=[1,2,0,1,0,0,0,0]
list1.sort()
reslut=[]
for i in range(len(list1)):
    if list1[i]==list1[i-1]:
        continue
    l = i+1
    r = len(list1) - 1
    if list1[0]>0:
        print('没有三元组')
        break
    else:
        while l<r:
            sum=list1[i]+list1[l]+list1[r]
            if sum == 0:
                reslut.append([list1[i], list1[l], list1[r]])
                while l<r and list1[l]==list1[l+1]:
                    l+=1
                while l<r and list1[r]==list1[r-1]:
                    r-=1
                l+=1
                r-=1
            elif sum<0:
                l+=1
            else:
                r-=1
print(reslut)






#方式2
# list1=[-1,0,1,2,-1,-4]
# sum_num=0
# dict_test={}
# san1=[]
# if sum(list1) ==0 and len(list1)==3 and list1[0]!=list1[1]:
#     print(list1)
# if list1==[0,0,0]:
#     print(list1)
# for i in range(len(list1)):
#     total=sum_num-list1[i]
#     for j in range(len(list1)):
#         if list1[j]+list1[i]==total and total in list1:
#             san1.append([list1[i],list1[j],total])
# print(san1)