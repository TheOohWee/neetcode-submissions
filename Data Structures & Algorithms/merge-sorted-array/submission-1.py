class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. shift things left n times
        # 2. read from nums2 into nums1
        # 3. sort
        copy = nums1[:]

        p1 = n
        p2 = 0
        while p1 < n + m:
            nums1[p1] = copy[p2]
            p1 += 1
            p2 += 1
        
        p3 = 0
        while p3 < n:
            nums1[p3] = nums2[p3]
            p3 += 1

        nums1.sort()