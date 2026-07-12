class Solution:
    def rotate(self, nums: List[int], k : int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l 

        tmp1 = nums[l - k: l]
        tmp2 = nums[0:l - k]
        nums[:] = tmp1 + tmp2