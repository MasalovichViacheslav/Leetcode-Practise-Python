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


