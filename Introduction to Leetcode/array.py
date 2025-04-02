# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array&
'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
2 <= nums.length <= 104
-10 ** 9 <= nums[i] <= 10 ** 9
-10 ** 9 <= target <= 10 ** 9

Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from idlelib.debugobj_r import remote_object_tree_item

# Solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for ind, numb in enumerate(nums):
#             try:
#                 ind2 = nums.index(target - numb, ind + 1)
#             except ValueError:
#                 continue
#             else:
#                 ind1 = ind
#                 break
#         return [ind1, ind2]


# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/?envType=problem-list-v2&envId=array
'''
1909. Remove One Element to Make the Array Strictly Increasing

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one 
element, or false otherwise. If the array is already strictly increasing, return true.
The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
 

Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.


Example 2:
Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

Example 3:
Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
 

Constraints:
2 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''

# Solution
# class Solution(object):
#     def canBeIncreasing(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         counter_of_non_increasing_elements = 0
#         abnormal_pair_first_element_index = None
#
#         # adding one more element in order to avoid IndexError in checking condition "if nums[index] < nums[index + 1]:"
#         nums.append(1001)
#         for index in range(len(nums) - 1):
#             if counter_of_non_increasing_elements <= 1:
#                 if nums[index] < nums[index + 1]:
#                     continue
#                 else:
#                     counter_of_non_increasing_elements += 1
#                     abnormal_pair_first_element_index = index
#             else:
#                 # case when there are 2 decreasing elements
#                 return False
#
#         if abnormal_pair_first_element_index is None or abnormal_pair_first_element_index == 0:
#             # case when all elements or elements after first element are increasing
#             return True
#         elif nums[abnormal_pair_first_element_index - 1] < nums[abnormal_pair_first_element_index + 1] or nums[
#             abnormal_pair_first_element_index] < nums[abnormal_pair_first_element_index + 2]:
#             # case when deletion of first or second element in abnormal pair in the middle of array makes all other
#             # elements increasing
#             return True
#         else:
#             # other cases
#             return False

# # Testcases
# print([1,2,10,5,7], "-->", Solution().canBeIncreasing([1,2,10,5,7]))
# print([2,3,1,2], "-->", Solution().canBeIncreasing([2,3,1,2]))
# print([1,1,1], "-->", Solution().canBeIncreasing([1,1,1]))
# print([4,5,2,6,7,1], "-->", Solution().canBeIncreasing([4,5,2,6,7,1]))
# print([6,1,2,3,4], "-->", Solution().canBeIncreasing([6,1,2,3,4]))
# print([1,2,3,4,2], "-->", Solution().canBeIncreasing([1,2,3,4,2]))
# print([105,924,32,968], "-->", Solution().canBeIncreasing([105,924,32,968]))


