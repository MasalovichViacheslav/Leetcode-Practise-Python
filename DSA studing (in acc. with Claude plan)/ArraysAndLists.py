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


# https://leetcode.com/problems/move-zeroes/
'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero 
elements.

Note that you must do this in-place without making a copy of the array. 

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 10 ** 4
-2 ** 31 <= nums[i] <= 2 ** 31 - 1
'''
# Solution1
# from typing import List
#
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for ind in range(-1, -(len(nums)) - 1, -1):
#             if not nums[ind]:
#                 nums.append(nums.pop(ind))
#         return nums


# testcases
# solution = Solution()
# print(solution.moveZeroes([1,0,0,3,0,4]), '--> expected: ', [1,3,4,0,0,0])
# print(solution.moveZeroes([0,1,0,0,3,0,4]), '--> expected: ', [1,3,4,0,0,0,0])
# print(solution.moveZeroes([0,1,0,0,5,3,0,4]), '--> expected: ', [1,5,3,4,0,0,0,0])
# print(solution.moveZeroes([0,0,1,2,0,0,3,4,0,0]), '--> expected: ', [1,2,3,4,0,0,0,0,0,0])


# https://leetcode.com/problems/maximum-subarray/description/
'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum. 

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:
1 <= nums.length <= 10 ** 5
-10 ** 4 <= nums[i] <= 10 ** 4 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
'''
# from typing import List
#
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#
#         positive_seq_sum = 0
#         negative_seq_sum = 0
#         sums = []
#
#         for number in nums:
#
#             if number > 0:
#
#                 if negative_seq_sum:
#                     sums.append(negative_seq_sum)
#                     negative_seq_sum = 0
#
#                 if not positive_seq_sum:
#                     positive_seq_sum = number
#                 else:
#                     positive_seq_sum += number
#
#             elif number < 0:
#
#                 if positive_seq_sum:
#                     sums.append(positive_seq_sum)
#                     positive_seq_sum = 0
#
#                 if not negative_seq_sum:
#                     negative_seq_sum = number
#                 else:
#                     negative_seq_sum += number
#
#         if positive_seq_sum: sums.append(positive_seq_sum)
#         if negative_seq_sum: sums.append(negative_seq_sum)
#
#         if len(sums) == 0:
#             print('only zeros in nums')
#             return 0
#
#         print(nums)
#         print(sums)
#
#         max_sum = 0
#         subarray_sum = 0
#         for a_sum in sums:
#
#             if not subarray_sum and a_sum > 0:
#                 subarray_sum = a_sum
#                 if subarray_sum > max_sum: max_sum = subarray_sum
#
#             elif subarray_sum and a_sum < 0:
#                 subarray_sum += a_sum
#                 if subarray_sum <= 0: subarray_sum = 0
#
#             elif subarray_sum and a_sum > 0:
#                 subarray_sum += a_sum
#                 if subarray_sum > max_sum: max_sum = subarray_sum
#
#         if max_sum:
#             print('subarray is found')
#             return max_sum
#         else:
#             print('only negative numbers in nums, the biddgest negative is returned')
#             return max(nums)


# Testcases
# solution = Solution()
# print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), '--> expected: ', 6)
# print(solution.maxSubArray([1]), '--> expected: ', 1)
# print(solution.maxSubArray([-7,-2,-6]), '--> expected: ', -2)
# print(solution.maxSubArray([1,1,1]), '--> expected: ', 3)
# print(solution.maxSubArray([-2,-2,-2]), '--> expected: ', -2)
# print(solution.maxSubArray([0,0,-2]), '--> expected: ', 0)
# print(solution.maxSubArray([0,0,0]), '--> expected: ', 0)
# print(solution.maxSubArray([1,-2,4,-2,1]), '--> expected: ', 4)


# https://leetcode.com/problems/merge-sorted-array/
'''
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To 
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''
# #Solution1
# from typing import List
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         del nums1[m:m + n]
#         nums1.extend(nums2)
#         nums1.sort()
#
#
# # Solution2
# from typing import List
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#
#         for i in range(n): nums1[m + i] = nums2[i]
#         nums1.sort()
#
#
# # Solution3
# from typing import List
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:m + n] = nums2
#         nums1.sort()


# testcases
# solution = Solution()
# solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

