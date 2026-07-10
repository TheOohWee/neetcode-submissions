class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sums
        l = len(nums)
        count = {0: 1}
        answer = 0

        # store values
        prefix = [0] * (l + 1)

        for i in range(1, l + 1):
            prefix[i] += nums[i - 1] + prefix[i - 1]
         
            if prefix[i] - k in count:
                answer += count[prefix[i] - k]
            count[prefix[i]] = count.get(prefix[i], 0) + 1

        return answer
        



