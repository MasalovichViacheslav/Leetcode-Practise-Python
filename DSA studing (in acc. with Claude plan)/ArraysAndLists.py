# https://leetcode.com/problems/plus-one/
'''
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''
from numpy.ma.core import negative

# Solution1
# from typing import List
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         number = int(''.join([str(x) for x in digits]))
#         number += 1
#         return [int(digit) for digit in str(number)]

# Solution2
# from typing import List
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for ind in range(len(digits) - 1, -1, -1):
#             if ind == len(digits) - 1:
#                 in_memory = (digits[ind] + 1) // 10
#                 digits[ind] = (digits[ind] + 1) % 10
#                 if not in_memory:
#                     return digits
#             else:
#                 in_memory, digits[ind] = ((digits[ind] + in_memory) // 10), ((digits[ind] + in_memory) % 10)
#                 if not in_memory:
#                     return digits
#         if in_memory:
#             digits.insert(0, in_memory)
#         return digits

# testcases
# solution = Solution()
# print(solution.plusOne([1,2,3]), '--> expected: ', [1,2,4])
# print(solution.plusOne([4,3,2,1]), '--> expected: ', [4,3,2,2])
# print(solution.plusOne([9]), '--> expected: ', [1,0])
# print(solution.plusOne([9,9]), '--> expected: ', [1,0,0])
# print(solution.plusOne([9,9,8,9,9]), '--> expected: ', [9,9,9,0,0])
# print(solution.plusOne([9,9,9,9,9]), '--> expected: ', [1,0,0,0,0,0])


