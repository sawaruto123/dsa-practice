"""
Problem: Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

Statement (in my own words):
The problem just wants us to check if there is a duplicate in the array.

My first approach:
First I was thinking about using something like a set to find them in the array and compare it with the list, but it didn't work as in cases where they are all unique it still stays true. Additionally, returning inside the loop terminated the code on the first iteration.

Final approach:
For the final approach, I figured out that I can just compare the len of set(nums) and nums. If they are the same, then there's no duplicate. With this logic, all I have to do is return if it's true or false.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)

