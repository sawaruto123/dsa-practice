"""
Problem: Valid Anagram (https://leetcode.com/problems/valid-anagram/)

Statement (in my own words):
The problem need us to be able to see the two string have the same letters and same counts of letters.

My first approach:
First i was thinking about comparing each element, then i went up google to look up methods.
I tried set operations but it didn't work as how i wish, so i looked up for another method.

Final approach:
For the final approach, i found the easiest way was actually just to sort
both string in the same way and see does they equal, which really was much more easier.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False

