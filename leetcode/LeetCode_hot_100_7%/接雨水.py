"""
@Author:sunqiyu
@Time:2026/6/29
@Desc:这个是文档注释，代码说明------
"""
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
'''
#算加上雨水的总面积-每个黑方块的面积=就是接到的雨水
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# #每个黑方块的面积
# sum_num=sum(height)
# # print(sum_num)
# #每一行的面积
#
# sum_num_all=0
# #找x行
# x=max(height)
# #每一层
# for j in range(1,x+1):
#     l = 1
#     r = len(height)
#     #找每一层的面积
#     for i in range(len(height)):
#         if height[i]:
#             l = min(i,l)
#         if height[i]:
#             r = max(i, r)
#     sum_num_all+=r-l
# print(sum_num_all)
# print(sum_num_all-sum_num)

height = [0,1,0,2,1,0,1,3,1,1,2,1]
sum_num = sum(height)
max_h = max(height)
sum_all = 0

# 逐层遍历，从第1层到最高层
for level in range(1, max_h + 1):
    left = None
    right = None
    # 找出当前层左右边界
    for idx, h in enumerate(height):
        if h >= level:
            if left is None:
                left = idx
            right = idx
    # 存在左右围墙才能存水
    if left is not None and right is not None:
        sum_all += right - left+1
rain = sum_all - sum_num
print(rain)  # 输出4不是6