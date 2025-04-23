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


# https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
'''
1399. Count Largest Group

You are given an integer n.
Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1. 

Constraints:
1 <= n <= 10 ** 4
'''
# from collections import defaultdict, Counter
#
# class Solution:
#     def countLargestGroup(self, n: int) -> int:
#         dd = defaultdict(list)
#         for number in range(1, n + 1):
#             if number < 10:
#                 digits_sum = number
#             elif 10 <= number <= 99:
#                 digits_sum = number // 10 + number % 10
#             elif 100 <= number <= 999:
#                 digits_sum = number // 100 + number // 10 % 10 + number % 10
#             elif 1000 <= number <= 9999:
#                 digits_sum = number // 1000 + number // 100 % 10 + number // 10 % 10 + number % 10
#             else:
#                 digits_sum = 1
#
#             dd[digits_sum].append(number)
#
#         groups_lens = [len(x) for x in dd.values()]
#         counter = Counter(groups_lens)
#
#         return counter[max(counter)]

# testcases
# solution = Solution()
# print(solution.countLargestGroup(13), 'expected:', 4)
# print(solution.countLargestGroup(2), 'expected:', 2)


