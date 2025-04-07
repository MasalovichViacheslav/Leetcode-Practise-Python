# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=problem-list-v2&envId=hash-table
'''
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a
string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the
strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.


Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

# # Solution
# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         if s1 == s2:
#             return True
#         chars = []
#         not_matching_counter = 0
#         for index in range(len(s1)):
#             if s1[index] != s2[index]:
#                 not_matching_counter += 1
#                 if not_matching_counter > 2:
#                     return False
#                 chars.extend((s1[index], s2[index]))
#         if not_matching_counter == 2 and chars[0] == chars[3] and chars[1] == chars[2]:
#             return True
#         else:
#             return False
#
# # Testcases
# print(Solution().areAlmostEqual('bank', 'kanb'), '-->', True)
# print(Solution().areAlmostEqual('attack', 'defend'), '-->', False)
# print(Solution().areAlmostEqual('kelb', 'kelb'), '-->', True)


# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/?envType=problem-list-v2&envId=hash-table
'''
2423. Remove Letter To Equalize Frequency

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and 
remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false 
otherwise.

Note:
The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.

Example 1:
Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

Example 2:
Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice 
versa. It is impossible to make all present letters have equal frequency.
 

Constraints:
2 <= word.length <= 100
word consists of lowercase English letters only.
'''
# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         char_dict = {}
#         for char in word:
#             char_dict[char] = char_dict.get(char, 0) + 1
#         print(char_dict)
#
#         # the word consists of the same letter
#         if len(char_dict) == 1:
#             print('1st True')
#             return True
#         # the word consists of two letter and one of them presented only once
#         elif len(char_dict) == 2 and 1 in char_dict.values():
#             print('2nd True')
#             return True
#         # the word consists of three or more letters and each of them presented once
#         elif all([True for v in char_dict.values() if v == 1]) and \
#                 len([True for v in char_dict.values() if v == 1]) == len(char_dict.values()):
#             print('3rd True')
#             return True
#         # the word consists of three or more letters, one of them presented once, other equally repeated
#         elif 1 in char_dict.values() and len([v for v in char_dict.values() if v == max(
#                 char_dict.values())]) == len(char_dict.values()) - 1:
#             print('4th True')
#             return True
#         # the word consists of two or more letter and one of them repeated 1 time more than each of others
#         elif len([v for v in char_dict.values() if v != max(char_dict.values())]) == len(char_dict.values()) - 1 and \
#             max(char_dict.values()) - min(char_dict.values()) == 1:
#             print('5th True')
#             return True
#
#         return False

# Testcases
# print(Solution().equalFrequency("abcc"), '-->', True)
# print(Solution().equalFrequency("aazz"), '-->', False)
# print(Solution().equalFrequency("az"), '-->', True)
# print(Solution().equalFrequency("azd"), '-->', True)
# print(Solution().equalFrequency("aa"), '-->', True)
# print(Solution().equalFrequency("aabbccdddeee"), '-->', False)
# print(Solution().equalFrequency("abbcc"), '-->', True)
# print(Solution().equalFrequency("cbccca"), '-->', False)
# print(Solution().equalFrequency("cccd"), '-->', True)
# print(Solution().equalFrequency("aaaabbbbccc"), '-->', False)


# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=problem-list-v2&envId=hash-table
'''
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :
1. i != j
2. 0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''

#Solution 1
# from typing import List
#
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         for ind in range(len(arr) - 1):
#             try:
#                 # arr[i] > arr[j]
#                 arr.index(arr[ind] / 2, ind + 1)
#                 print('1st try', arr.index(arr[ind] / 2, ind + 1), ind)
#                 return True
#             except ValueError:
#                 try:
#                     # arr[j] > arr[i]
#                     arr.index(arr[ind] * 2, ind + 1)
#                     print('2nd try', arr.index(arr[ind] * 2, ind + 1), ind)
#                     return True
#                 except ValueError:
#                     continue
#         return False

#Solution 2
# from typing import List
# from collections import Counter
#
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         numb_dict = Counter(arr)
#         for numb in numb_dict:
#             if numb == 0 and numb_dict[numb] > 1:
#                 return True
#             if numb_dict[numb * 2] and numb != 0 or numb_dict[numb * 2] and numb != 0:
#                 return True
#         return False

# Testcases
# print(Solution().checkIfExist([10,2,5,3]), '-->', True)
# print(Solution().checkIfExist([3,1,7,11]), '-->', False)
# print(Solution().checkIfExist([-6,-3,1,7,11]), '-->', True)
# print(Solution().checkIfExist([-6,1,7,11,-3]), '-->', True)
# print(Solution().checkIfExist([1,7,11,-6,-3]), '-->', True)
# print(Solution().checkIfExist([0,1,7,0,3]), '-->', True)
# print(Solution().checkIfExist([1,7,0,3,0]), '-->', True)
# print(Solution().checkIfExist([7,1,14,11]), '-->', True)
# print(Solution().checkIfExist([7,15,3,4,30]), '-->', True)
# print(Solution().checkIfExist([-2,0,10,-19,4,6,-8]), '-->', False)
# print(Solution().checkIfExist([-20,8,-6,-14,0,-19,14,4]), '-->', True)


# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=problem-list-v2&envId=hash-table
'''
3487. Maximum Unique Subarray Sum After Deletion

You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, 
select a subarray of nums such that:

1. All elements in the subarray are unique.
2. The sum of the elements in the subarray is maximized.
3. Return the maximum sum of such a subarray.
 

Example 1:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation:
Select the entire array without deleting any element to obtain the maximum sum.

Example 2:
Input: nums = [1,1,0,1,1]
Output: 1
Explanation:
Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain 
the maximum sum.

Example 3:
Input: nums = [1,2,-1,-2,1,0,-1]
Output: 3
Explanation:
Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain 
the maximum sum.
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
'''

#Solution
# from typing import List
#
#
# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         non_negative = {x for x in nums if x >= 0}
#         if non_negative:
#             return sum(non_negative)
#         else:
#             negative = {x for x in nums if x < 0}
#             return max(negative)
#
# # Testcases
# print(Solution().maxSum([1,2,3,4,5]), '-->', 15)
# print(Solution().maxSum([1,1,0,1,1]), '-->', 1)
# print(Solution().maxSum([1,2,-1,-2,1,0,-1]), '-->', 3)
# print(Solution().maxSum([-6,-1,-2]), '-->', -1)
# print(Solution().maxSum([-6,0,-1,-2]), '-->', 0)
# print(Solution().maxSum([-6]), '-->', -6)
# print(Solution().maxSum([6]), '-->', 6)
# print(Solution().maxSum([0]), '-->', 0)


