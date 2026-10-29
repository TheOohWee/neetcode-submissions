class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = []
        for i in matrix:
            c += i
        
        low, high = 0, len(c) - 1

        while low <= high:
            m = (low + high) // 2
            if c[m] == target:
                return True
            elif c[m] >= target:
                high = m - 1
            else:
                low = m + 1
        
        return False
