# https://leetcode.com/problems/roman-to-integer/
'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''
# # Solution1
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         symb_val = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
#                     'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
#
#         number = 0
#         skip = False
#         for ind in range(len(s)):
#             if skip:
#                 skip = False
#                 continue
#             elif s[ind: ind + 2] in symb_val:
#                 number += symb_val[s[ind: ind + 2]]
#                 skip = True
#             else:
#                 number += symb_val[s[ind]]
#
#         return number
#
# # Solution2
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         symb_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#         number = 0
#         current = s[-1]
#         for symbol in s[::-1]:
#             if current != symbol:
#                 if symb_val[symbol] >= symb_val[current]:
#                     number += symb_val[symbol]
#                 else:
#                     number -= symb_val[symbol]
#                 current = symbol
#             else:
#                 number += symb_val[symbol]
#
#         return number

# testcases
# solution = Solution()
# print(solution.romanToInt("III"), 'expected:', 3)
# print(solution.romanToInt("LVIII"), 'expected:', 58)
# print(solution.romanToInt("MCMXCIV"), 'expected:', 1994)
# print(solution.romanToInt("IX"), 'expected:', 9)
# print(solution.romanToInt("I"), 'expected:', 1)
# print(solution.romanToInt("XCIX"), 'expected:', 99)


# https://leetcode.com/problems/contains-duplicate/
'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every 
element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 

Constraints:
1 <= nums.length <= 10 ** 5
-10 ** 9 <= nums[i] <= 10 ** 9
'''
# # Solution1
# from typing import List
#
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return False
#
#         return not len(nums) == len(set(nums))


# https://leetcode.com/problems/group-anagrams/description/
'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10 ** 4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
# #Solution1
# from typing import List
# from collections import Counter
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         res = [[strs[0]]]
#         for word in strs[1:]:
#             for group in res:
#                 if len(word) == len(group[0]):
#                     if Counter(word) == Counter(group[0]):
#                         group += [word]
#                         break
#             else:
#                 res += [[word]]
#
#         return res
#
# #Solution2
# from typing import List
# from itertools import groupby
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         sorted_strs = sorted(strs, key=lambda x: sorted(Counter(x).items()))
#         res = [list(group) for key, group in groupby(sorted_strs, key=lambda x: sorted(Counter(x).items()))]
#
#         return res
#
# #Solution3
# from typing import List
# from collections import defaultdict
#
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         dd = defaultdict(list)
#         for word in strs:
#             key = [x for x in word]
#             key.sort()
#             dd[''.join(key)].append(word)
#
#         return list(dd.values())

# testcases
# solution = Solution()
# print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), 'expected: ', [["bat"],["nat","tan"],["ate","eat","tea"]])
# print(solution.groupAnagrams([""]), 'expected: ', [[""]])


# https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear 
as many times as it shows in both arrays and you may return the result in any order. 

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into t
he memory at once?
'''
# from typing import List
# from collections import Counter
#
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#
#         if len(nums1) >= len(nums2):
#             longer, shorter = nums1, nums2
#         else:
#             longer, shorter = nums2, nums1
#
#         longer_counter = Counter(longer)
#         shorter_counter = Counter(shorter)
#
#         res = []
#         for number, repeats in shorter_counter.items():
#             if number in longer_counter:
#                 res += [number] * min(repeats, longer_counter[number])
#
#         return res

# testcases
# solution = Solution()
# print(solution.intersect([1,2,2,1], [2,2]), 'expected:', [2,2])
# print(solution.intersect([4,9,5], [9,4,9,8,4]), 'expected:', [9,4])
# print(solution.intersect([1,2], [1,1]), 'expected:', [1])

