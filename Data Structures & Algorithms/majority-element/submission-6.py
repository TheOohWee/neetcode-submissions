class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) 

        # since i need to return a num then the outer loop is gonna be a num
        for num in nums: 
            count = 0
            for i in range(len(nums)):
                if nums[i] == num:
                    count += 1
            if count > n // 2:
                return num