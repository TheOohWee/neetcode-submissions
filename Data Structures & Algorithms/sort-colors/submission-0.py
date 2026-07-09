class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        tmp = []
        for num in nums:
            if num == 0:
                tmp.append(num)
        for num in nums:
            if num == 1:
                tmp.append(num)
        for num in nums:
            if num == 2:
                tmp.append(num)
        
        nums[:] = tmp 
            
