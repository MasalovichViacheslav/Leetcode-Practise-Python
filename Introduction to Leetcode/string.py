# https://leetcode.com/problems/slowest-key/description/?envType=problem-list-v2&envId=string
'''
1629. Slowest Key

A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence,
and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed.
The 0th key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was
released.

The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of
releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].

Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same
key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the
lexicographically largest key of the keypresses.



Example 1:

Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"
Explanation: The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and
released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character
and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and
 released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.

Example 2:
Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explanation: The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.


Constraints:

releaseTimes.length == n
keysPressed.length == n
2 <= n <= 1000
1 <= releaseTimes[i] <= 10 ** 9
releaseTimes[i] < releaseTimes[i+1]
keysPressed contains only lowercase English letters.
'''
# from calendar import leapdays, isleap
# from math import remainder
# from string import punctuation

#Solution
# from typing import List
#
# class Solution:
#     def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
#
#         for index in range(len(keysPressed)):
#             if index == 0:
#                 max_duration = releaseTimes[index]
#                 max_duration_key = keysPressed[index]
#             else:
#                 if releaseTimes[index] - releaseTimes[index - 1] > max_duration:
#                     max_duration = releaseTimes[index] - releaseTimes[index - 1]
#                     max_duration_key = keysPressed[index]
#                 elif releaseTimes[index] - releaseTimes[index - 1] == max_duration and keysPressed[
#                     index] > max_duration_key:
#                     max_duration = releaseTimes[index] - releaseTimes[index - 1]
#                     max_duration_key = keysPressed[index]
#
#         return max_duration_key

# #Testcases
# print(Solution().slowestKey([12,23,36,46,62], "spuda"), '-->', 'a')
# print(Solution().slowestKey([9,29,49,50], "cbcd"), '-->', 'c')
# print(Solution().slowestKey([5,15], "cc"), '-->', 'c')
# print(Solution().slowestKey([5,10,15], "abc"), '-->', 'c')


# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/?envType=problem-list-v2&envId=string
'''
2047. Number of Valid Words in a Sentence

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', 
and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more 
spaces ' '.

A token is a valid word if all three of the following are true:

1. It only contains lowercase letters, hyphens, and/or punctuation (no digits).
2. There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab"
 and "ab-" are not valid).
3. There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are 
valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

Example 1:
Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".

Example 2:
Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.

Example 3:
Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
 

Constraints:
1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.
'''

# # Solution
# class Solution:
#     def countValidWords(self, sentence: str) -> int:
#         tokens_list = sentence.split(' ')
#         valid_words_counter = 0
#
#         for token in tokens_list:
#             if token != '':
#                 hyphen_counter = 0
#                 for index in range(len(token)):
#                     if token[index].isdigit():
#                         break
#                     elif token[index] == '-':
#                         if index == 0 or index == len(token) - 1:
#                             break
#                         elif token[index - 1].isalpha() and token[index + 1].isalpha():
#                             hyphen_counter += 1
#                             if hyphen_counter > 1:
#                                 break
#                         else:
#                             break
#                     elif token[index] in ('!', '.', ',') and index != len(token) - 1:
#                         break
#                 else:
#                     valid_words_counter += 1
#         return valid_words_counter
#
# # Testcases
# print(Solution().countValidWords("cat and  dog"), '-->', 3)
# print(Solution().countValidWords("!this  1-s b8d!"), '-->', 0)
# print(Solution().countValidWords("!"), '-->', 1)
# print(Solution().countValidWords(" "), '-->', 0)
# print(Solution().countValidWords("  "), '-->', 0)
# print(Solution().countValidWords(" !"), '-->', 1)
# print(Solution().countValidWords(" !!"), '-->', 0)
# print(Solution().countValidWords(" 55"), '-->', 0)
# print(Solution().countValidWords(" !-a"), '-->', 0)
# print(Solution().countValidWords("dog spider-man, spider-cat-dog"), '-->', 2)
# print(Solution().countValidWords("! a-b, -ab ab-"), '-->', 2)
# print(Solution().countValidWords("ab, cd! . a!b c.,"), '-->', 3)
# print(Solution().countValidWords("-"), '-->', 0)
# sent = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
# print(Solution().countValidWords(sent), '-->', 49)


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=string
'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack. 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 10 ** 4
haystack and needle consist of only lowercase English characters.
'''

# Solution 1 - too Introduction to Leetcode
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

# Solution 2
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle not in haystack:
#             return -1
#         else:
#             for index in range(len(haystack)):
#                 if haystack[index] == needle[0] and haystack[index: index + len(needle)] == needle:
#                     return index


# Testcases
# print(Solution().strStr('sadbutsad', 'sad'), '-->', 0)
# print(Solution().strStr('leetcode', 'leeto'), '-->', -1)
# print(Solution().strStr('s', 's'), '-->', 0)
# print(Solution().strStr('s', 'c'), '-->', -1)


# https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string
'''
168. Excel Sheet Column Title
 
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 2 ** 31 - 1
'''

# Solution
# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         alphabet_generator = (chr(x) for x in range(65, 91))
#         dictionary = dict(zip(range(1, 27), alphabet_generator))
#         column_title = ''
#
#         while columnNumber > 0:
#             division_remainder = columnNumber % 26
#             if division_remainder != 0:
#                 column_title += dictionary[division_remainder]
#                 columnNumber //= 26
#             else:
#                 column_title += dictionary[26]
#                 columnNumber = columnNumber // 26 - 1
#
#         return column_title[::-1]


# Testcases
# print(Solution().convertToTitle(1), '-->', 'A')
# print(Solution().convertToTitle(28), '-->', 'AB')
# print(Solution().convertToTitle(52), '-->', 'AZ')
# print(Solution().convertToTitle(53), '-->', 'BA')
# print(Solution().convertToTitle(702), '-->', 'ZZ')
# print(Solution().convertToTitle(703), '-->', 'AAA')
# print(Solution().convertToTitle(16384), '-->', 'XFD')


# https://leetcode.com/problems/day-of-the-year/description/?envType=problem-list-v2&envId=string
'''
1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31st, 2019.
'''

# Solution
# class Solution:
#     def dayOfYear(self, date: str) -> int:
#         # yyyy_mm_dd_list = list(map(int, date.split('-')))
#         yyyy_mm_dd_list = [int(elem) for elem in date.split('-')]
#         month_duration_leap_year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#         month_duration_non_leap_year = month_duration_leap_year.copy()
#         month_duration_non_leap_year[2] = 28
#
#         days_passed = 0
#         if yyyy_mm_dd_list[0] % 4 == 0 and (yyyy_mm_dd_list[0] % 100 != 0 or yyyy_mm_dd_list[0] % 400 == 0):
#             if yyyy_mm_dd_list[1] == 1:
#                 days_passed = yyyy_mm_dd_list[2]
#             else:
#                 for month in range(1, yyyy_mm_dd_list[1]):
#                     days_passed += month_duration_leap_year[month]
#                 days_passed += yyyy_mm_dd_list[2]
#         else:
#             if yyyy_mm_dd_list[1] == 1:
#                 days_passed = yyyy_mm_dd_list[2]
#             else:
#                 for month in range(1, yyyy_mm_dd_list[1]):
#                     days_passed += month_duration_non_leap_year[month]
#                 days_passed += yyyy_mm_dd_list[2]
#
#         return days_passed
#
# # Testcases
# print(Solution().dayOfYear("2019-01-09"), '-->', 9)
# print(Solution().dayOfYear("2020-01-09"), '-->', 9)
# print(Solution().dayOfYear("2000-03-10"), '-->', 70)
# print(Solution().dayOfYear("2001-03-10"), '-->', 69)


# https://leetcode.com/problems/repeated-substring-pattern/description/?envType=problem-list-v2&envId=string
'''
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the 
substring together.

 

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 10 ** 4
s consists of lowercase English letters.
'''
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         if len(s) == 1:
#             return False
#         elif len(s) == 2 and s[0] != s[1]:
#             return False
#         substring = ''
#         for index in range(int(len(s) / 2 + 1) - 1):
#             substring += s[index]
#             if s.replace(substring, '') == '':
#                 return True
#         return False
#
# # Testcases
# print(Solution().repeatedSubstringPattern('abab'), '-->', True)
# print(Solution().repeatedSubstringPattern('aba'), '-->', False)
# print(Solution().repeatedSubstringPattern('abcabcabcabc'), '-->', True)
# print(Solution().repeatedSubstringPattern('a'), '-->', False)
# print(Solution().repeatedSubstringPattern('aa'), '-->', True)
# print(Solution().repeatedSubstringPattern('aaa'), '-->', True)
# print(Solution().repeatedSubstringPattern('ab'), '-->', False)


# https://leetcode.com/problems/number-of-segments-in-a-string/description/?envType=problem-list-v2&envId=string
'''
434. Number of Segments in a String

Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
 

Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
'''
# class Solution:
#     def countSegments(self, s: str) -> int:
#         return len(s.split())
#
# # testcases
# print(Solution().countSegments("Hello, my name is John"), '-->', 5)
# print(Solution().countSegments(''), '-->', 0)
# print(Solution().countSegments("Hello"), '-->', 1)

