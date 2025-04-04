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


