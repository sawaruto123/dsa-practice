"""
Problem: Two Sum[](https://leetcode.com/problems/two-sum/)

Statement (in my own words):
The problem requires finding two numbers in a given list that add up to a specific target value. 
We need to return the indices of these two numbers.

My first approach:
The first thing I got stuck on was forgetting how Python works, but I still tried to get the logic right. 
My initial attempt was to use nested for loops to compare all elements and find which pair matches the target.

Final approach:
For the final solution, I followed an explanation from YouTube[](https://www.youtube.com/watch?v=KLlXCFG5TnA). 
I realised that a faster way is to calculate the difference (target - current number) and check if that difference 
already exists in a hash map (dictionary) that stores previously seen numbers and their indices.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}  # val : index

        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[j] = i
        return
