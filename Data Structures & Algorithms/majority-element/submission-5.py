class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = sorted(nums)

        return s[len(s)//2]

            