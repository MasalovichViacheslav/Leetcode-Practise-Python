# https://leetcode.com/problems/longest-common-prefix/
'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

# Solution1
# from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         common_prefix = ''
#         for letters in zip(*strs):
#             letter = set(letters)
#             if len(letter) == 1:
#                 common_prefix += letters[0]
#             else:
#                 return common_prefix
#         return common_prefix

# testcases
# solution = Solution()
# print(solution.longestCommonPrefix(["flower","flow","flight"]), '-->', 'fl')
# print(solution.longestCommonPrefix(["flower","","flight"]), '-->', '')
# print(solution.longestCommonPrefix(["flower","flower","flower"]), '-->', 'flower')
# print(solution.longestCommonPrefix(["dog","racecar","car"]), '-->', '')


# https://leetcode.com/problems/length-of-last-word/
'''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
 

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

# # Solution1
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(str.split(s)[-1])
#
# # Solution2
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         length = 0
#         for index in range(-1, -(len(s)) - 1, -1):
#             if s[index].isalpha():
#                 length = length + 1
#             elif length and not s[index].isalpha():
#                 return length
#         return length

# testcases
# solution = Solution()
# print(solution.lengthOfLastWord("Hello World"), '-->', 5)
# print(solution.lengthOfLastWord("   fly me   to   the moon  "), '-->', 4)
# print(solution.lengthOfLastWord("luffy is still joyboy"), '-->', 6)


# https://leetcode.com/problems/valid-anagram/
'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 10 ** 4
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
# Solution1
# from collections import Counter
#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s_counter = Counter(s)
#         t_counter = Counter(t)
#
#         return not any((s_counter - t_counter).values())


#Solution2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s_list = [x for x in s]
#         s_list.sort()
#         t_list = [y for y in t]
#         t_list.sort()
#
#         return s_list == t_list

# testcases
# solution = Solution()
# print(solution.isAnagram("anagram", "nagaram"), 'expected:', True)
# print(solution.isAnagram("rat", "car"), 'expected:', False)

# https://leetcode.com/problems/longest-palindromic-substring/
'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s. 

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb" 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
# Solution 1
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == s[::-1]:
#             return s
#
#         counter = {}
#         for index, char in enumerate(s):
#             if char in counter:
#                 counter[char].append(index)
#             else:
#                 counter[char] = [index]
#
#         max_palindrome = s[0]
#         for char in counter:
#             while counter[char]:
#                 for index in counter[char][1:]:
#                     subarray = s[counter[char][0]:index + 1]
#                     if subarray == subarray[::-1] and len(subarray) > len(max_palindrome):
#                         max_palindrome = subarray
#                 del counter[char][0]
#
#         return max_palindrome

# Solution2
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == s[::-1]:
#             return s
#
#         max_palindrome = s[0]
#         may_be_palindrome = ''
#         for char in s:
#             if may_be_palindrome == may_be_palindrome[::-1] and len(may_be_palindrome) > len(max_palindrome):
#                 max_palindrome = may_be_palindrome
#
#             if (may_be_palindrome + char)[::-1] in s:
#                 may_be_palindrome += char
#
#             else:
#                 while may_be_palindrome:
#                     may_be_palindrome = may_be_palindrome[1:]
#                     if (may_be_palindrome + char)[::-1] in s:
#                         break
#                 may_be_palindrome += char
#
#         if may_be_palindrome == may_be_palindrome[::-1] and len(may_be_palindrome) > len(max_palindrome):
#             max_palindrome = may_be_palindrome
#
#         return max_palindrome

# testcases
# solution = Solution()
# print(solution.longestPalindrome('34abcdcbcdcbaf'), 'expected', 'abcdcbcdcba')
# print(solution.longestPalindrome('3aba4cdcbcdcbaf'), 'expected', 'cdcbcdc')
# print(solution.longestPalindrome('cdc'), 'expected', 'cdc')
# print(solution.longestPalindrome('acdc'), 'expected', 'cdc')
# print(solution.longestPalindrome('babad'), 'expected', 'bab')
# print(solution.longestPalindrome('cbbd'), 'expected', 'bb')
# print(solution.longestPalindrome('aacabdkacaa'), 'expected', 'aca')
# print(solution.longestPalindrome('abacab'), 'expected', 'bacab')


