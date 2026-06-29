"""
@Author:sunqiyu
@Time:2026/6/25
@Desc:这个是文档注释，代码说明------
"""
'''
定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
'''
#暴力破解
# height=[1,8,6,2,5,4,8,3,7]
# max_sum=0
# for i in  range(len(height)):
#     for j in range(len(height)):
#         now_sum=min(height[i],height[j])*(i-j)
#         if max_sum<now_sum:
#             max_sum=now_sum
# print(max_sum)

#双指针
height=[1,8,6,2,5,4,8,3,7]
max_sum=0
i0 , i=0 , len(height)-1
while i0<i:
    now_sum=(i-i0)*min(height[i],height[i0])
    max_sum=max(max_sum,now_sum)
    if height[i0]<=height[i]:
        i0+=1
    else:
        i-= 1
print(max_sum)
'''
height=[1,4,6,2,5,4,8,3,7]
max_height=max(height)
twomax_height=0
left=0
right=len(height)
max_with=left-right
for i in range(len(height)):
    if height[i] == max_height:
        left=i
    if twomax_height ==


print(max_with*max_height)
'''
