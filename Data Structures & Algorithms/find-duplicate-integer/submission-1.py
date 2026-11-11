class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = len(nums) * [0]

        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1