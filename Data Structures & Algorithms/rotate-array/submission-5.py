class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k % len(nums)):
            tmp = nums[len(nums) - 1]
            copy = nums[:]

            for i in range(len(nums) - 1):
                nums[i + 1] = copy[i]
            nums[0] = tmp