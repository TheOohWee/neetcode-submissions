class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        i = 0
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
            i += 1
        
        return list(res)