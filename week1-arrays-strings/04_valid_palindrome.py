"""
Problem: Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)

Statement (in my own words):
The problem wants us to see if the value can be a palindrome if they are all lowercase and removed anything other than letters and
numbers.

My first approach:
I first started by forming the string by removing all unneeded parts, then chopping it in half and comparing the left and right parts, which
to be honest I was already quite close. The only mistake I made here was trying to use sorted to compare, but two of them having the same
set of letters doesn't mean that they are in the correct order to form a palindrome.

Final approach:
My last step was really just finding the command to just invert the right side then return if they ==

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def isPalindrome(self, s):
        p = "".join(char for char in s.lower() if char.isalnum())
        middle = len(p)//2
        left = p[:middle]
        right = p[len(p) - middle:]
        return left == right[::-1]


