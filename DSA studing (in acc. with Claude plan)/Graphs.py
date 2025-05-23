# https://leetcode.com/problems/flood-fill/description/
'''
733. Flood Fill

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of
the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image
starting from the pixel image[sr][sc].

To perform a flood fill:

1. Begin with the starting pixel and change its color to color.
2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
 either horizontally or vertically) and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it
matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of
the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation:
The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to
the image.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2**16
0 <= sr < m
0 <= sc < n
'''
# from typing import List
# from collections import deque
#
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m, n = len(image) - 1, len(image[0]) - 1
#         start_color = image[sr][sc]
#         pixels = deque()
#         pixels.append((sr, sc))
#
#         if start_color != color:
#             while pixels:
#                 row, column = pixels.popleft()
#                 image[row][column] = color
#                 if row - 1 >= 0 and image[row - 1][column] == start_color:
#                     pixels.append((row - 1, column))
#                 if row + 1 <= m and image[row + 1][column] == start_color:
#                     pixels.append((row + 1, column))
#                 if column - 1 >= 0 and image[row][column - 1] == start_color:
#                     pixels.append((row, column - 1))
#                 if column + 1 <= n and image[row][column + 1] == start_color:
#                     pixels.append((row, column + 1))
#
#         return image
#
#
# # testcases
# solution = Solution()
# print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), 'expected:', [[2,2,2],[2,2,0],[2,0,1]])
# print(solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0), 'expected:', [[0,0,0],[0,0,0]])


# https://leetcode.com/problems/find-the-town-judge/description/
'''
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person 
labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise. 

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1 

Constraints:
1 <= n <= 1000
0 <= trust.length <= 10**4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''
# Solution1
# from typing import List
# from collections import defaultdict

# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#
#         if n == 1 and not trust:
#             return 1
#
#         dd = defaultdict(list)
#
#         for person1, person2 in trust:
#             dd[person2].append(person1)
#
#         for potential_judge, persons_trust in dd.items():
#             if len(persons_trust) == n - 1:
#                 break
#         else:
#             return -1
#
#         for persons_trust in dd.values():
#             if potential_judge in persons_trust:
#                 return -1
#
#         return potential_judge



# testcases
# solution = Solution()
# print(solution.findJudge(2, [[1,2]]), 'expected:', 2)

