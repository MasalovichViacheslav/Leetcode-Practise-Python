# https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''
703. Kth Largest Element in a Stream

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in
real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit
their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously
returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth
highest score in the sorted list of all scores.

Implement the KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
- int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element
in the pool of test scores so far.

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8


Constraints:

0 <= nums.length <= 10**4
1 <= k <= nums.length + 1
-10**4 <= nums[i] <= 10**4
-10**4 <= val <= 10**4
At most 10**4 calls will be made to add.
'''
# # Solution1
# from typing import List
# import heapq
#
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         heapq.heapify(nums)
#         self.scores = nums
#         self.kth_score = k
#
#     def add(self, val: int) -> int:
#         heapq.heappush(self.scores, val)
#         return heapq.nlargest(self.kth_score, self.scores)[-1]
#
# # Solution2
# from typing import List
# import heapq
#
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         heapq.heapify(nums)
#         self.all_scores = nums
#         self.k = k
#         if k <= len(nums):
#             self.k_scores = heapq.nlargest(k, nums)
#             heapq.heapify(self.k_scores)
#         else:
#             self.k_scores = None
#
#     def add(self, val: int) -> int:
#         if not self.k_scores:
#             heapq.heappush(self.all_scores, val)
#             if self.k == len(self.all_scores):
#                 self.k_scores = self.all_scores
#             return self.all_scores[0]
#         else:
#             if val > self.k_scores[0]:
#                 heapq.heapreplace(self.k_scores, val)
#             return self.k_scores[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# https://leetcode.com/problems/top-k-frequent-elements/description/
'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any 
order. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
# Solution1
# from typing import List
# from collections import Counter
# import heapq
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_repeats = Counter(nums)
#         the_heap = []
#         for num, repeats in nums_repeats.items():
#             heapq.heappush(the_heap, (repeats, num))
#         return [pair[1] for pair in heapq.nlargest(k, the_heap)]
#
# # Solution2
# from typing import List
# from collections import Counter
# import heapq
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_repeats = Counter(nums)
#         the_heap = []
#
#         for num, repeats in nums_repeats.items():
#             if len(the_heap) < k:
#                 heapq.heappush(the_heap, (repeats, num))
#             elif repeats >= the_heap[0][0]:
#                 heapq.heapreplace(the_heap, (repeats, num))
#         return [pair[1] for pair in heapq.nlargest(k, the_heap)]
#
# # Solution3
# from typing import List
# from collections import Counter
# import heapq
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_repeats = Counter(nums)
#         the_heap = []
#
#         for num, repeats in nums_repeats.items():
#             if len(the_heap) < k:
#                 heapq.heappush(the_heap, (repeats, num))
#             elif repeats >= the_heap[0][0]:
#                 heapq.heapreplace(the_heap, (repeats, num))
#         return [pair[1] for pair in the_heap]
#
#
#
# solution = Solution()
#
# print(solution.topKFrequent([3,0,1,0], 1))


# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
'''
# Solution1
# from typing import List
# import heapq
#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         the_heap = []
#         for num in nums:
#             if len(the_heap) < k:
#                 heapq.heappush(the_heap, num)
#             elif num > the_heap[0]:
#                 heapq.heapreplace(the_heap, num)
#         return the_heap[0]


# https://leetcode.com/problems/k-closest-points-to-origin/description/
'''
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k 
closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:
1 <= k <= points.length <= 10**4
-10**4 <= xi, yi <= 10**4
'''
#Solution1
# from typing import List
# from math import sqrt
#
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         return [elem[1] for elem in sorted(((sqrt(x**2 + y**2), [x, y]) for x, y in points))[:k]]
#
# #Solution2
# from typing import List
# import heapq
# from math import sqrt
#
#
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         the_heap = []
#         for point in points:
#             distance = sqrt(point[0] ** 2 + point[1] ** 2)
#             if len(the_heap) < k:
#                 heapq.heappush(the_heap, (-distance, point))
#             elif -distance > the_heap[0][0]:
#                 heapq.heapreplace(the_heap, (-distance, point))
#         return [elem[1] for elem in the_heap]


