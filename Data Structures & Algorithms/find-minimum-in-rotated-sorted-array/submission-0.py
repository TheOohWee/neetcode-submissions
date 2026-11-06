class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        for i in nums:
            if i < m:
                m = i
        
        return m