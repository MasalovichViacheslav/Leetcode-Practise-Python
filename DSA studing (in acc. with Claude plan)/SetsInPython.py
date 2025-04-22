# https://leetcode.com/problems/intersection-of-two-arrays/
'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
# from typing import List
#
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1).intersection(set(nums2)))


# https://leetcode.com/problems/happy-number/
'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not 
include 1.
3. Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 2 ** 31 - 1
'''
# class Solution:
#     def isHappy(self, n: int) -> bool:
#
#         previous_ns = set()
#         new_ns = {n}
#
#         while previous_ns != new_ns:
#             squares = [int(x) ** 2 for x in str(n)]
#             n = sum(squares)
#             if n == 1:
#                 return True
#             previous_ns = new_ns.copy()
#             new_ns.update({n})
#
#         return False
#
# # testcases
# solution = Solution()
# print(solution.isHappy(19), 'expected:', True)
# print(solution.isHappy(2), 'expected:', False)
# print(solution.isHappy(0), 'expected:', False)
# print(solution.isHappy(1), 'expected:', True)


# https://leetcode.com/problems/missing-number/
'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is 
missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the 
range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it 
does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the 
range since it does not appear in nums.
 

Constraints:
n == nums.length
1 <= n <= 10 ** 4
0 <= nums[i] <= n
All the numbers of nums are unique.
 
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
# # solution1
# from typing import List
#
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for number in range(len(nums) + 1):
#             if number not in nums:
#                 return number
#
# # solution2
# from typing import List
#
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         return int(len(nums) * (len(nums) + 1) / 2 - sum(nums))
#
# # testcases
# solution = Solution()
# print(solution.missingNumber([3,0,1]), 'expected:', 2)
# print(solution.missingNumber([0,1]), 'expected:', 2)
# print(solution.missingNumber([9,6,4,2,3,5,7,0,1]), 'expected:', 8)


