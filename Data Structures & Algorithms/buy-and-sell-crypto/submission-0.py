class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [...]
        # prices[i], where i is the day
        # return max 
        max = 0

        # 1. brute force approach
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max
