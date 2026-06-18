class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash map solution
        n = len(nums)
        i = 0

        counts = {}

        for num in nums: 
            counts[num] = counts.get(num, i) + 1 

        return max(counts, key = counts.get)

            