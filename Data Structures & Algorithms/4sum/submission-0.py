class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        a = 0
        while a < len(nums):
            b = a + 1
            while b < len(nums):
                c, d = b + 1, len(nums) - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                b += 1
            a += 1


        return list(res)


