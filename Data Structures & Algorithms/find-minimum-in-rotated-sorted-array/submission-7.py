class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            m = (l + r) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                res = min(nums[m], res)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res


        
