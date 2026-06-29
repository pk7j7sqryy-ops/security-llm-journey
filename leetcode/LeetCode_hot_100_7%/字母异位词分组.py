"""
@Author:sunqiyu
@Time:2026/6/22
@Desc:这个是文档注释，代码说明------
"""
from collections import defaultdict

'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        将字母异位词组合在一起
        
        Args:
            strs: 字符串数组
            
        Returns:
            包含字母异位词分组的列表
        """
        # 使用字典来存储分组结果，键为排序后的字符串，值为该组的所有原始字符串
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 将字符串排序作为键，字母异位词排序后会得到相同的字符串
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        
        # 返回所有分组的值
        return list(anagram_map.values())

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict_test={}
for i in strs:
    str_test=''.join(sorted(i))
    if str_test not in dict_test:
        dict_test[str_test]=[]
    dict_test[str_test].append(i)
print(list(dict_test.values()))
    # for x in str_test:
    #     if x in i:




'''0


解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]


提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
'''
