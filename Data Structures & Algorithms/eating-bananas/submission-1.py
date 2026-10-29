from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2
            s = 0
            for i in piles:
                s += ceil(i/k)
            if s <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        
        return res