# https://leetcode.com/problems/sort-an-array/
"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and
with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.


Constraints:

1 <= nums.length <= 5 * 10**4
-5 * 10**4 <= nums[i] <= 5 * 10**4
"""
from tokenize import group

# Solution 1
# from typing import List
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.merge_sort(nums)
#
#     def merge(self, left, right):
#
#         l_ind = r_ind = 0
#         merged = []
#
#         while l_ind < len(left) and r_ind < len(right):
#             if left[l_ind] <= right[r_ind]:
#                 merged.append(left[l_ind])
#                 l_ind += 1
#             else:
#                 merged.append((right[r_ind]))
#                 r_ind += 1
#
#         while l_ind < len(left):
#             merged.extend(left[l_ind:])
#             break
#
#
#         while r_ind < len(right):
#             merged.extend((right[r_ind:]))
#             break
#
#         return merged
#
#
#     def merge_sort(self, array):
#
#         if len(array) < 2:
#             return array
#
#         middle = len(array) // 2
#
#         return self.merge(
#             left=self.merge_sort(array[:middle]),
#             right=self.merge_sort(array[middle:])
#         )

# Solution 2 (Memory Limit Exceeded for big nums)
# from typing import List
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.quick_sort(nums)
#
#
#     def quick_sort(self, array):
#
#         if len(array) < 2:
#             return array
#
#         left, same, right = [], [], []
#
#         pivot = array[len(array) // 2]
#
#         for elem in array:
#             if elem < pivot:
#                 left.append(elem)
#             elif elem == pivot:
#                 same.append(elem)
#             else:
#                 right.append(elem)
#
#         return self.quick_sort(left) + same + self.quick_sort(right)

# Solution 3
# from typing import List
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.timsort(nums)
#
#
#     def timsort(self, array):
#
#         run = 32
#         arr_len = len(array)
#
#         for start_ind in range(0, arr_len, run):
#             for i in range(start_ind + 1, min(start_ind+run, arr_len)):
#                 key_item = array[i]
#                 j = i - 1
#
#                 while j >= start_ind and array[j] > key_item:
#                     array[j + 1] = array[j]
#                     j -= 1
#
#                 array[j + 1] = key_item
#
#         size = run
#
#         while size <= arr_len:
#             for n in range(0, arr_len, size * 2):
#                 left_start, left_end = n, min(arr_len, n + size)
#                 right_start, right_end = min(arr_len, n + size), min(arr_len, n + size * 2)
#
#                 left_subarray = array[left_start: left_end]
#                 right_subarray = array[right_start: right_end]
#
#                 left_ind, right_ind = 0, 0
#
#                 while left_ind < len(left_subarray) and right_ind < len(right_subarray):
#                     if left_subarray[left_ind] <= right_subarray[right_ind]:
#                         array[n] = left_subarray[left_ind]
#                         n += 1
#                         left_ind += 1
#                     else:
#                         array[n] = right_subarray[right_ind]
#                         n += 1
#                         right_ind += 1
#
#                 while left_ind < len(left_subarray):
#                     array[n] = left_subarray[left_ind]
#                     n += 1
#                     left_ind += 1
#
#                 while right_ind < len(right_subarray):
#                     array[n] = right_subarray[right_ind]
#                     n += 1
#                     right_ind += 1
#
#             size *= 2
#
#         return array
#
# # testcases
# solution = Solution()
# # print(solution.sortArray([5,2,3,1]), 'expected:', [1,2,3,5])
# # print(solution.sortArray([5,1,1,2,0,0]), 'expected:', [0,0,1,1,2,5])
# nums = [
#     -74,  48, -20,   2,  10, -84,  -5,  -9,  11, -24,
#     -91,   2, -71,  64,  63,  80,  28, -30, -58, -11,
#     -44, -87, -22,  54, -74, -10, -55, -28, -46,  29,
#      10,  50, -72,  34,  26,  25,   8,  51,  13,  30,
#      35,  -8,  50,  65,  -6,  16,  -2,  21, -78,  35,
#     -13,  14,  23,  -3,  26, -90,  86,  25, -56,  91,
#     -13,  92, -25,  37,  57, -20, -69,  98,  95,  45,
#      47,  29,  86, -28,  73, -44, -46,  65, -84, -96,
#     -24, -12,  72, -68,  93,  57,  92,  52, -45,  -2,
#      85, -63,  56,  55,  12, -85,  77, -39
# ]
#
# sorted_nums = [
#     -96, -91, -90, -87, -85, -84, -84, -78, -74, -74,
#     -72, -71, -69, -68, -63, -58, -56, -55, -46, -46,
#     -45, -44, -44, -39, -30, -28, -28, -25, -24, -24,
#     -22, -20, -20, -13, -13, -12, -11, -10,  -9,  -8,
#      -6,  -5,  -3,  -2,  -2,   2,   2,   8,  10,  10,
#      11,  12,  13,  14,  16,  21,  23,  25,  25,  26,
#      26,  28,  29,  29,  30,  34,  35,  35,  37,  45,
#      47,  48,  50,  50,  51,  52,  54,  55,  56,  57,
#      57,  63,  64,  65,  65,  72,  73,  77,  80,  85,
#      86,  86,  91,  92,  92,  93,  95,  98
# ]
# print(solution.sortArray(nums), '\nexpected:\n', sorted_nums, f'\nresult is as expected - {nums == sorted_nums}')


# https://leetcode.com/problems/sort-colors/description/
"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color 
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
# Solution 1
# from typing import List
#
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(1, len(nums)):
#             current_color = nums[i]
#             j = i - 1
#
#             while j >= 0 and nums[j] > current_color:
#                 nums[j + 1] = nums[j]
#                 j -= 1
#
#             nums[j + 1] = current_color

# Solution 2
# from typing import List
#
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         last_red_ind = None
#
#
#         for i in range(1, len(nums)):
#             current_color = nums[i]
#             if current_color == 0 and not last_red_ind:
#                 j = i - 1
#
#                 while j >= 0 and nums[j] > current_color:
#                     nums[j + 1] = nums[j]
#                     j -= 1
#
#                 nums[j + 1] = current_color
#                 last_red_ind = j + 1
#
#             elif current_color == 0:
#                 nums[last_red_ind + 1: i + 1] = [nums[i]] + nums[last_red_ind + 1: i]
#                 last_red_ind += 1
#
#             else:
#                 j = i - 1
#
#                 while j >= 0 and nums[j] > current_color:
#                     nums[j + 1] = nums[j]
#                     j -= 1
#
#                 nums[j + 1] = current_color

# solution = Solution()
# nums = [2,0,2,1,1,0]
# print(nums)
# solution.sortColors(nums)
# print("sorted:\n", nums, sep='')
# nums = [2,0,1]
# print(nums)
# solution.sortColors(nums)
# print("sorted:\n", nums, sep='')



# https://leetcode.com/problems/merge-intervals/description/
"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
 

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 10**4
intervals[i].length == 2
0 <= starti <= endi <= 10**4
"""
# Solution 1
# from typing import List
#
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         result = [intervals[0]]
#
#         for ind in range(1, len(intervals)):
#             if result[-1][1] >= intervals[ind][0]:
#                 if result[-1][1] < intervals[ind][1]:
#                     result[-1][1] = intervals[ind][1]
#             else:
#                 result.append(intervals[ind])
#
#         return result
#
# solution = Solution()
# print(solution.merge([[1,3],[2,6],[8,10],[15,18]]), 'expected:', [[1,6],[8,10],[15,18]])
# print(solution.merge([[1,4],[4,5]]), 'expected:', [[1,5]])
# print(solution.merge([[1,4],[2,3]]), 'expected:', [[1,4]])


# https://leetcode.com/problems/largest-number/description/
"""
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 10**9
"""
# Solution 1
# from typing import List
#
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#
#         only_zeros = True
#
#         nums[0] = str(nums[0])
#
#         if nums[0] != '0':
#             only_zeros = False
#
#         for i in range(1, len(nums)):
#             nums[i] = str(nums[i])
#             current_num = nums[i]
#             if current_num != '0':
#                 only_zeros = False
#             j = i - 1
#
#             while j >= 0 and nums[j] + current_num < current_num + nums[j]:
#                 nums[j + 1] = nums[j]
#                 j -= 1
#
#             nums[j + 1] = current_num
#
#         return ''.join(nums) if only_zeros is False else '0'

# Solution 2
# from typing import List
#
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#
#         without_duplicates = set(nums)
#         if len(without_duplicates) == 1 and 0 in without_duplicates:
#             return '0'
#
#         return ''.join(self.str_quick_sort([str(num) for num in nums]))
#
#     def str_quick_sort(self, str_array: str):
#
#         if len(str_array) < 2:
#             return str_array
#
#         smaller, same, bigger = [], [], []
#
#         pivot = str_array[len(str_array) // 2]
#
#         for elem in str_array:
#             if elem + pivot > pivot + elem:
#                 bigger.append(elem)
#             elif elem + pivot == pivot + elem:
#                 same.append(elem)
#             else:
#                 smaller.append(elem)
#
#         return self.str_quick_sort(bigger) + same + self.str_quick_sort(smaller)


# solution = Solution()
# print(solution.largestNumber([10,2]), "expected:", "210")
# print(solution.largestNumber([3,30,34,5,9]), "expected:", "9534330")
# print(solution.largestNumber([0,0]), "expected:", "0")
# print(solution.largestNumber([30,34,9,98,99,998,9,0]), "expected:", "99999989834300")
# nums = [
#        4,   1,   8,  10,   9,   4,   4,   3,   4,   4,
#        3,  10, 100,   1,   7,  53,  89,  39,  76,  43,
#       28,  22,  85,  65,  44,  57,  50,  39,  11,  64,
#       26,  71,  85,  48,  11,  57,  59,  43,  87,  92,
#      374, 216, 539, 901, 510, 940, 102, 853, 535, 266,
#      556, 461, 163, 725, 475, 337, 234, 337, 568, 653,
#      330, 988, 629, 900, 808, 803, 373, 444, 906, 167,
#      950, 102, 197, 806, 542, 769, 281, 566, 439, 973,
#      847, 429, 689, 301, 823, 756, 707, 241, 545, 320,
#      579, 533, 527, 107, 659, 175, 796, 374, 194, 993,
# ]
# print(solution.largestNumber(nums), "expected:", "9...")
# print(solution.largestNumber([9, 993]), 'expected:', '9993')



