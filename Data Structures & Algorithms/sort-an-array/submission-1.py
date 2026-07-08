import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            pivot = random.choice(nums)
            less = [i for i in nums if i < pivot]
            equal = [i for i in nums if i == pivot]
            greater = [i for i in nums if i > pivot]
            return self.sortArray(less) + equal + self.sortArray(greater)
