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


