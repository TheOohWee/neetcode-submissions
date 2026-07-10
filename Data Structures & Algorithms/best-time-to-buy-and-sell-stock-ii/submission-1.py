class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP2 = 0

        i = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                profit = prices[i+1] - prices[i]
                maxP2 += profit
            i += 1

        return maxP2

