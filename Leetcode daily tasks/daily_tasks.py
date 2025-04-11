# https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11
'''
2843. Count Symmetric Integers

You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the
last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].



Example 1:
Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.

Constraints:
1 <= low <= high <= 10 ** 4
'''

# Solution 1
# class Solution:
#     def countSymmetricIntegers(self, low: int, high: int) -> int:
#         count = 0
#         for number in range(low, high + 1):
#             str_number = str(number)
#             if len(str_number) % 2 == 0:
#                 half1 = str_number[:int(len(str_number) / 2)]
#                 half2 = str_number[int(len(str(number)) / 2):]
#                 if sum(int(x) for x in half1) == sum(int(x) for x in half2):
#                     count += 1
#         return count

# Solution 2
# class Solution:
#     def countSymmetricIntegers(self, low: int, high: int) -> int:
#         count = 0
#         for number in range(low, high + 1):
#
#             if 10 <= number <= 99 and number % 10 == number // 10:
#                 count += 1
#
#             elif 1000 <= number <= 9999:
#                 dig1 = number // 1000
#                 dig2 = number // 100 % 10
#                 dig3 = number // 10 % 10
#                 dig4 = number % 10
#                 if dig1 + dig2 == dig3 + dig4:
#                     count += 1
#
#         return count


# Testcases
# solution = Solution()
# print(solution.countSymmetricIntegers(1, 100), '-->', 9)
# print(solution.countSymmetricIntegers(1200, 1230), '-->', 4)
# print(solution.countSymmetricIntegers(1000, 3899), '-->', 198)


