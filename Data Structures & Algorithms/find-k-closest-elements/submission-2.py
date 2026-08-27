class Solution:
    def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(a) - k

        while l < r:
            m = (l + r) // 2
            if abs(a[m] - x) > abs(a[m + k] - x):
                l = m + 1
            else:
                r = m

        return a[l:l+k]