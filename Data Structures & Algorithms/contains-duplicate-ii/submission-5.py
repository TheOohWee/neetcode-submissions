class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if i > k:
                seen.discard(nums[i - k - 1])
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True

        return False



