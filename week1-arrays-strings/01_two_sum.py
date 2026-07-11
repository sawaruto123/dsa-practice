"""
Problem: Two Sum (LeetCode #1)
https://leetcode.com/problems/two-sum/

Statement (in my own words):
Given a list of numbers and a target, find the indices of the two numbers
that add up to the target. Only one valid answer exists.

My first approach:
Brute force - check every pair with two nested loops. Works, but it's
O(n^2), and it "feels" wrong because I'm re-checking numbers I've already
seen every single time.

Final approach:
Walk through the list once. For each number, check if (target - number)
has already been seen. If yes, we found our pair. If no, remember this
number's index for later. This works because by the time we reach the
second number of a valid pair, the first number is already stored.

Time complexity: O(n) - single pass
Space complexity: O(n) - the hash map in the worst case stores every number
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # no solution found (shouldn't happen per problem constraints)


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # expected [0, 1]
    print(two_sum([3, 2, 4], 6))        # expected [1, 2]
    print(two_sum([3, 3], 6))           # expected [0, 1]
