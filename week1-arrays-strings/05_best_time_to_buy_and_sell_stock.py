"""
Problem: Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Statement (in my own words):
The question just want you to find is there any way in the list that you can make profit, if so what is the max profit.

My first approach:
First i was trying sort but then realise that it will mess up the order of the date.

Final approach:
Then i move on focusing on finding the lower prize and compare it to i and find the biggest max profit and print it out

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price

        return max_profit


