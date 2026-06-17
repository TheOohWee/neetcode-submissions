class Solution: 
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in nums: 
            if i != val:
                k += 1
        
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
            
        return k