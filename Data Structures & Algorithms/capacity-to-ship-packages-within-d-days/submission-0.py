class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            ships = 1
            cap = m
            for w in weights:
                if cap - w < 0:
                    cap = m
                    ships += 1
                cap = cap - w
            return ships <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
             
            
