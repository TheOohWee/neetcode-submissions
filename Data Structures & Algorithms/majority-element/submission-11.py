class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore voting algorithm? 
        res = count = 0

        for num in nums: 
            if count == 0:
                res = num
                count = 1
            elif num == res:
                count += 1
            elif num != res:
                count -= 1
        return res