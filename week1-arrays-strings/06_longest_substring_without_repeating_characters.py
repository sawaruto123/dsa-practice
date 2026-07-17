"""
Problem: Longest Substring Without Repeating Characters
(https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Statement (in my own words):
The question wants us to find the length of the possible longest substring base on the input.

My first approach:
At first as i didnt really knew about substring, i thought i can get it done by just len(set()). But it didnt work, as the order and whenever the letter is connect need to be respected.

Final approach:
In the end i just go with referring a list i create to double if the current i is same as what's saved on the list and splitting the list when found so.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        anw = []
        max_length = 0

        for char in s:
            if char in anw:
                dup_index = anw.index(char)
                anw = anw[dup_index + 1:]

            anw.append(char)

            if len(anw) > max_length:
                max_length = len(anw)

        return max_length


