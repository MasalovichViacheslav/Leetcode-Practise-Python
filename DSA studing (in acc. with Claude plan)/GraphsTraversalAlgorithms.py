# https://leetcode.com/problems/number-of-islands/
'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
# Solution1
# from typing import List
# from collections import deque
#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         areas = deque([(0, 0)])
#         visited = set()
#         island_qty = 0
#
#         while areas:
#             row_ind, col_ind = areas.popleft()
#             if (row_ind, col_ind) in visited:
#                 continue
#             visited.add((row_ind, col_ind))
#
#             if grid[row_ind][col_ind] == "1":
#                 island = deque([(row_ind, col_ind)])
#                 island_qty += 1
#                 while island:
#                     r_ind, c_ind = island.popleft()
#                     visited.add((r_ind, c_ind))
#                     for r_change, c_change in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#                         new_r = r_ind + r_change
#                         new_c = c_ind + c_change
#                         if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited and (new_r, new_c) not in island:
#                             island.append((new_r, new_c)) if grid[new_r][new_c] == "1" else areas.append((new_r, new_c))
#             else:
#                 for row_change, col_change in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#                     new_row = row_ind + row_change
#                     new_col = col_ind + col_change
#                     if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited and (new_row, new_col) not in areas:
#                         areas.append((new_row, new_col))
#
#         return island_qty


# testcases
# solution = Solution()
# sample_grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# print(solution.numIslands(sample_grid), 'expected:', 1)
# sample_grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(solution.numIslands(sample_grid), 'expected:', 3)
# sample_grid = [["1"]]
# print(solution.numIslands(sample_grid), 'expected:', 1)
# sample_grid = [["0"]]
# print(solution.numIslands(sample_grid), 'expected:', 0)
# sample_grid =[["0","1","0"],["1","0","1"],["0","1","0"]]
# print(solution.numIslands(sample_grid), 'expected:', 4)
# sample_grid = [
#     ["0","0","0","0","0","0","0","0","0"],
#     ["0","0","1","1","1","1","1","0","0"],
#     ["0","0","1","0","0","0","1","0","0"],
#     ["0","0","1","0","1","0","1","0","0"],
#     ["0","0","1","0","0","0","1","0","0"],
#     ["0","0","1","1","1","1","1","0","0"],
#     ["0","0","0","0","0","0","0","0","0"]
# ]
# print(solution.numIslands(sample_grid), 'expected:', 2)
# for row in sample_grid:
#     print(row)

# sample_grid = [
#     ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
#     ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
#     ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
#     ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
#     ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
#     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
# ]
# print(solution.numIslands(sample_grid), 'expected:', )


# https://leetcode.com/problems/max-area-of-island/description/
"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
# Solution1
# from typing import List, Tuple
#
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         visited = set()
#         island = []
#         max_island_size = 0
#         directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
#
#         def explore_island(position: Tuple[int]) -> int:
#             island.append(position)
#             size = 0
#             while island:
#                 row, col = island.pop()
#                 visited.add((row, col))
#                 size += 1
#                 for row_change, col_change in directions:
#                     new_row = row + row_change
#                     new_col = col + col_change
#                     if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1 and \
#                             (new_row, new_col) not in visited:
#                         island.append((new_row, new_col))
#                         visited.add((new_row, new_col))
#             return size
#
#         for row_ind in range(m):
#             for col_ind in range(n):
#                 if grid[row_ind][col_ind] == 1 and (row_ind, col_ind) not in visited:
#                     new_island_size = explore_island((row_ind, col_ind))
#                     if max_island_size < new_island_size:
#                         max_island_size = new_island_size
#
#         return max_island_size
#
# # testcases
# solution = Solution()
# sample_grid = [
#     [0,0,1,0,0,0,0,1,0,0,0,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,1,1,0,1,0,0,0,0,0,0,0,0],
#     [0,1,0,0,1,1,0,0,1,0,1,0,0],
#     [0,1,0,0,1,1,0,0,1,1,1,0,0],
#     [0,0,0,0,0,0,0,0,0,0,1,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# print(solution.maxAreaOfIsland(sample_grid), "expected:", 6)
#
# sample_grid = [[0,0,0,0,0,0,0,0]]
# print(solution.maxAreaOfIsland(sample_grid), "expected:", 0)


