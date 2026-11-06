class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            r -= 1
        
        return nums[r + 1] if r + 1 < len(nums) else nums[l]