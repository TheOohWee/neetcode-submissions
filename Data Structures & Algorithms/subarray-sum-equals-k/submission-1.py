class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums) + 1
        prefix = [0] * l
        d = {0: 1}
        ans = 0

        for i in range(1, l):
            prefix[i] += prefix[i - 1] + nums[i - 1]

            # prefix[i] - prefix[j] = k
            # prefix[i] - k = prefix[j]
            if prefix[i] - k in d:
                ans += d[prefix[i] - k]
            d[prefix[i]] = d.get(prefix[i], 0) + 1 

        return ans