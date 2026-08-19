class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        length = float('inf')

        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                length = min(length, r - l + 1)
                cur -= nums[l]
                l += 1
        
        return length if length != float('inf') else 0