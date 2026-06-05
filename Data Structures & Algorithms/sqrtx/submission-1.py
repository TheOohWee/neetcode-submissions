class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x 

        while low <= high:
            g = (low + high) // 2
            if g * g == x:
                return g
            elif g * g < x:
                low = g + 1
            elif g * g > x:
                high = g - 1

        return high