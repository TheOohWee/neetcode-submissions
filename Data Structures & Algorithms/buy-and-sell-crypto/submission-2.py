class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        r = 0 # sell
        l = 0 # buy
        max = 0

        while r < len(prices):
            if prices[r] - prices[l] > max:
                max = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max


