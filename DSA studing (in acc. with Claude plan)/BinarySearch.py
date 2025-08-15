# https://leetcode.com/problems/binary-search/
"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 10**4
-10**4 < nums[i], target < 10**4
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from numpy.matrixlib.defmatrix import matrix

# Solution 1
# from typing import List
# import bisect
#
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         index = bisect.bisect_left(nums, target)
#         if index < len(nums) and nums[index] == target:
#             return index
#         else:
#             return -1


# Solution 2
# from typing import List
#
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#
#         low, high = 0, len(nums) - 1
#
#         while high >= low:
#
#             middle = (low + high) // 2
#
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#
#         return -1


# Solution 3
# from typing import List
#
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def binary_search(nums, target, low, high):
#
#             if low >= high and nums[low] != target:
#                 return -1
#
#             middle = (low + high) // 2
#
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#
#             return binary_search(nums, target, low, high)
#
#         return binary_search(nums, target, low=0, high=(len(nums) - 1))


# testcases
# solution = Solution()
# print(solution.search([-1,0,3,5,9,12], 9), 'expected:', 4)
# print(solution.search([-1,0,3,5,9,12], 2), 'expected:', -1)
# print(solution.search([3], 9), 'expected:', -1)
# print(solution.search([3], 3), 'expected:', 0)
# print(solution.search([2,5], 0), 'expected:', -1)
# print(solution.search([2,5], 6), 'expected:', -1)



# https://leetcode.com/problems/search-insert-position/description/
"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums contains distinct values sorted in ascending order.
-10**4 <= target <= 10**4
"""
# Solution 1
# from typing import List
# import bisect
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         return bisect.bisect_left(nums, target)


# Solution 2
# from typing import List
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low, high = 0, len(nums) - 1
#
#         while high - low > 1:
#             middle = (low + high) // 2
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#
#         if nums[low] >= target:
#             return low
#         elif nums[high] >= target:
#             return high
#         else:
#             return high + 1


# Solution 3
# from typing import List
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         def recursive_search(nums, target, low, high):
#
#             if high - low <= 1:
#                 return low, high
#
#             middle = (low + high) // 2
#
#             if nums[middle] == target:
#                 return middle,
#             elif nums[middle] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#
#             return recursive_search(nums, target, low, high)
#
#         recursion_result = recursive_search(nums, target, low=0, high=len(nums) - 1)
#
#         if len(recursion_result) == 1:
#             return recursion_result[0]
#         else:
#             final_low, final_high = recursion_result
#             if nums[final_low] >= target:
#                 return final_low
#             elif nums[final_high] >= target:
#                 return final_high
#             else:
#                 return final_high + 1

# testcases
# solution = Solution()
# print(solution.searchInsert([1,3,5,6], 5), "expected:", 2)
# print(solution.searchInsert([1,3,5,6], 2), "expected:", 1)
# print(solution.searchInsert([1,3,5,6], 7), "expected:", 4)
# print(solution.searchInsert([1,3,8,11,12,20,23,30], 22), "expected:", 6)



# https://leetcode.com/problems/search-a-2d-matrix/description/
"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
1) Each row is sorted in non-decreasing order.
2) The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10**4 <= matrix[i][j], target <= 10**4
"""
# Solution 1
# from typing import List
# import bisect
#
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#
#         if target > matrix[-1][-1] or target < matrix[0][0]:
#             return False
#
#         row_ind = bisect.bisect_left(matrix, target, key=lambda x: x[0])
#
#         if row_ind > len(matrix) - 1:
#             row = matrix[row_ind - 1]
#         elif matrix[row_ind][0] == target:
#             return True
#         else:
#             row = matrix[row_ind - 1]
#
#         index = bisect.bisect_left(row, target)
#         if index <= len(row) - 1 and row[index] == target:
#             return True
#         else:
#             return False

# Solution 2
# from typing import List
#
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m_low, m_high = 0, len(matrix) - 1
#
#         while m_high >= m_low:
#             middle = (m_high + m_low) // 2
#             if matrix[middle][0] == target:
#                 return True
#             elif matrix[middle][0] > target:
#                 m_high = middle - 1
#             else:
#                 m_low = middle + 1
#
#         if m_low == 0:
#             row_ind = m_low
#         else:
#             row_ind = m_low - 1
#
#         row = matrix[row_ind]
#
#         r_low, r_high = 0, len(row) - 1
#
#         while r_high >= r_low:
#             middle = (r_high + r_low) // 2
#
#             if row[middle] == target:
#                 return True
#             elif row[middle] > target:
#                 r_high = middle - 1
#             else:
#                 r_low = middle + 1
#
#         return False


# Solution 3
# from typing import List
#
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def search_row_ind(matrix, target, low, high):
#
#             if low > high:
#                 return low
#
#             middle = (low + high) // 2
#
#             if matrix[middle][0] == target:
#                 return True
#             elif matrix[middle][0] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#
#             return search_row_ind(matrix, target, low, high)
#
#         result = search_row_ind(matrix, target, low=0, high=len(matrix) - 1)
#
#         if type(result) is bool:
#             return True
#         else:
#             row_ind = result
#
#         if row_ind == 0:
#             row = matrix[row_ind]
#         else:
#             row = matrix[row_ind - 1]
#
#         def search_target_in_row(row, target, r_low, r_high):
#             if r_low > r_high:
#                 return False
#
#             middle = (r_low + r_high) // 2
#
#             if row[middle] == target:
#                 return True
#             elif row[middle] > target:
#                 r_high = middle - 1
#             else:
#                 r_low = middle + 1
#
#             return search_target_in_row(row, target, r_low, r_high)
#
#         return search_target_in_row(row, target, r_low=0, r_high=len(row) - 1)


# solution = Solution()
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), 'expected:', True)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34), 'expected:', True)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), 'expected:', False)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0), 'expected:', False)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61), 'expected:', False)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1), 'expected:', True)
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11), 'expected:', True)
# print(solution.searchMatrix([[1,3,5,7]], 61), 'expected:', False)
# print(solution.searchMatrix([[1,3,5,7]], 5), 'expected:', True)
# print(solution.searchMatrix([[1],[11],[34]], 61), 'expected:', False)
# print(solution.searchMatrix([[1],[11],[34]], 11), 'expected:', True)
# print(solution.searchMatrix([[34]], 34), 'expected:', True)



