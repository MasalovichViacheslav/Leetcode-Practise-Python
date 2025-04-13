# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10 ** 5
0 <= prices[i] <= 10 ** 4
'''
# Solution 1 - exceeds time limit
# from typing import List
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for ind in range(len(prices) - 1):
#             potential_max_profit = max(prices[ind + 1:]) - prices[ind]
#             if potential_max_profit > max_profit:
#                 max_profit = potential_max_profit
#         return max_profit

# Solution 2
# from typing import List
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         min_price = 10000
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price
#         return max_profit


# # testcases
# solution = Solution()
# print(solution.maxProfit([7,1,5,3,6,4]), '--> expected:', 5)
# print(solution.maxProfit([7,6,4,3,1]), '--> expected:', 0)
# print(solution.maxProfit([7]), '--> expected:', 0)
# print(solution.maxProfit([0]), '--> expected:', 0)
# print(solution.maxProfit([0,1,4,7,3,9,0,10]), '--> expected:', 10)
# print(solution.maxProfit([10,1,4,7,3,9,0,20]), '--> expected:', 20)


# https://leetcode.com/problems/valid-parentheses/
'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true


Constraints:

1 <= s.length <= 10 ** 4
s consists of parentheses only '()[]{}'.
'''
# class Solution:
#     def isValid(self, s: str) -> bool:
#         bracket_closing_queue = []
#         opening = {'(': ')', '[': ']', '{': '}'}
#         if len(s) % 2 != 0:
#             return False
#
#         for bracket in s:
#             if bracket in opening:
#                 bracket_closing_queue.append(opening[bracket])
#             else:
#                 if not bracket_closing_queue:
#                     return False
#                 elif bracket != bracket_closing_queue[-1]:
#                     return False
#                 else:
#                     del bracket_closing_queue[-1]
#
#         if bracket_closing_queue:
#             return False
#         else:
#             return True
#
# # testcases
# solution = Solution()
# print(solution.isValid('()'), '--> expected:', True)
# print(solution.isValid('()[]{}'), '--> expected:', True)
# print(solution.isValid('(]'), '--> expected:', False)
# print(solution.isValid('([])'), '--> expected:', True)
# print(solution.isValid('{([}])'), '--> expected:', False)
# print(solution.isValid('{'), '--> expected:', False)
# print(solution.isValid('{({[])}}'), '--> expected:', False)


