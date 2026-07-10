class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # buy and sell
        maxP1 = 0
        maxP2 = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP1 = max(maxP1, profit)
            else:
                l = r
            r += 1

        i = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                profit = prices[i+1] - prices[i]
                maxP2 += profit
            i += 1

        return max(maxP1, maxP2)

