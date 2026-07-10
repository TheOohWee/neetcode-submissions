class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = defaultdict(int)
        res = set()

        for num in nums:
            d[num] += 1

        for num in nums:
            if d.get(num) > n // 3:
                res.add(num)

        return list(res)