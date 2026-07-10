class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 1

        if len(nums) == 0:
            return 0

        cur = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif abs(nums[i] - nums[i + 1]) == 1:
                cur += 1
                if longest < cur:
                    longest = cur 
            else:
                cur = 1
                
        return longest
        
        