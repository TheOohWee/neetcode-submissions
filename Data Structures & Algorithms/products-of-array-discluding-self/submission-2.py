class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            product = math.prod(left) * math.prod(right) 
            output.append(product)
        return output