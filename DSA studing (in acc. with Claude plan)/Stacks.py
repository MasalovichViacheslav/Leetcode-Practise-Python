# https://leetcode.com/problems/backspace-string-compare/
'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
'''
#Solution1
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_backspaced = []
#         for letter in s:
#             if letter.isalpha():
#                 s_backspaced.append(letter)
#             else:
#                 if s_backspaced:
#                     s_backspaced.pop()
#
#         t_backspaced = []
#         for letter in t:
#             if letter.isalpha():
#                 t_backspaced.append(letter)
#             else:
#                 if t_backspaced:
#                     t_backspaced.pop()
#
#         return s_backspaced == t_backspaced

#Solution2
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:


# testcases
# solution = Solution()
# print(solution.backspaceCompare('ab#c', 'ad#c'), 'expected', True)
# print(solution.backspaceCompare('ab##', 'c#d#'), 'expected', True)
# print(solution.backspaceCompare('a#c', 'b'), 'expected', False)
# print(solution.backspaceCompare('###a#c', 'b#c'), 'expected', True)


# https://leetcode.com/problems/remove-outermost-parentheses/description/
'''
1021. Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, 
and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, 
with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are 
primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

1 <= s.length <= 10 ** 5
s[i] is either '(' or ')'.
s is a valid parentheses string.
'''
# Solution1
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         stack = []
#         result = []
#         primitive = []
#         for bracket in s:
#             if bracket == "(":
#                 stack.append(bracket)
#                 primitive.append(bracket)
#             else:
#                 stack.pop()
#                 primitive.append(bracket)
#
#             if not stack and primitive:
#                 result.append(''.join(primitive[1:len(primitive) - 1]))
#                 primitive.clear()
#
#         return ''.join(result)

# Solution2
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         brackets_count = 0
#         result = ''
#         for bracket in s:
#             if not brackets_count and bracket == "(":
#                 brackets_count += 1
#             elif bracket == "(":
#                 brackets_count += 1
#                 result += bracket
#             elif brackets_count == 1 and bracket == ")":
#                 brackets_count -= 1
#             elif bracket == ")":
#                 brackets_count -= 1
#                 result += bracket
#
#         return result


# testcases
# solution = Solution()
# print(solution.removeOuterParentheses("(()())(())"), 'expected:', '()()()')
# print(solution.removeOuterParentheses("(()())(())(()(()))"), 'expected:', '()()()()(())')
# print(solution.removeOuterParentheses("()()"), 'expected:', '')


# https://leetcode.com/problems/daily-temperatures/
'''
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0] 

Constraints:
1 <= temperatures.length <= 10 * 5
30 <= temperatures[i] <= 100
'''
#Solution1
# from typing import List
#
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#
#         result = []
#         for ind, temp in enumerate(temperatures):
#             for index, temperature in enumerate(temperatures[ind + 1:], start=ind+1):
#                 if temperature > temp:
#                     result.append(index - ind)
#                     break
#             else:
#                 result.append(0)
#
#         return result
#
# #Solution2
# from typing import List
#
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#
#         non_increasing_stack = []
#         result = []
#
#         for index, temperature in enumerate(temperatures[:-1]):
#
#             if temperatures[index + 1] > temperature:
#                 result.append(1)
#                 while non_increasing_stack:
#                     if temperatures[index + 1] > non_increasing_stack[-1][1]:
#                         result[non_increasing_stack[-1][0]] = index + 1 - non_increasing_stack[-1][0]
#                         non_increasing_stack.pop()
#                     else:
#                         break
#             else:
#                 result.append(0)
#                 non_increasing_stack.append((index, temperature))
#
#         result.append(0)
#         return result
#
# # testcases
# solution = Solution()
# print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]), 'expected:', [1,1,4,2,1,1,0,0])
# print(solution.dailyTemperatures([30,40,50,60]), 'expected:', [1,1,1,0])
# print(solution.dailyTemperatures([30,60,90]), 'expected:', [1,1,0])
# print(solution.dailyTemperatures([90,60,30]), 'expected:', [0,0,0])
# print(solution.dailyTemperatures([90]), 'expected:', [0])

# https://leetcode.com/problems/min-stack/
'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:
-2**31 <= val <= 2**31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10 ** 4 calls will be made to push, pop, top, and getMin.
'''
# # Solution 1
# from collections import deque
#
# class MinStack:
#
#     def __init__(self):
#         self.tuplesStack = deque()
#
#     def push(self, val: int) -> None:
#         if not self.tuplesStack:
#             self.tuplesStack.append((val, val))
#         else:
#             if val < self.tuplesStack[-1][1]:
#                 self.tuplesStack.append((val, val))
#             else:
#                 self.tuplesStack.append((val, self.tuplesStack[-1][1]))
#
#     def pop(self) -> None:
#         self.tuplesStack.pop()
#
#     def top(self) -> int:
#         return self.tuplesStack[-1][0]
#
#     def getMin(self) -> int:
#         return self.tuplesStack[-1][1]

# Solution 2
# class MinStack:
#
#     def __init__(self):
#         self.tuplesStack = []
#
#     def push(self, val: int) -> None:
#         if not self.tuplesStack:
#             self.tuplesStack.append((val, val))
#         else:
#             if val < self.tuplesStack[-1][1]:
#                 self.tuplesStack.append((val, val))
#             else:
#                 self.tuplesStack.append((val, self.tuplesStack[-1][1]))
#
#     def pop(self) -> None:
#         self.tuplesStack.pop()
#
#     def top(self) -> int:
#         return self.tuplesStack[-1][0]
#
#     def getMin(self) -> int:
#         return self.tuplesStack[-1][1]


# minstack = MinStack()
# minstack.push(-2)
# minstack.push(0)
# minstack.push(-3)
# print(minstack.tuplesStack)
# print(minstack.getMin())
# minstack.pop()
# print(minstack.top())
# print(minstack.getMin())


