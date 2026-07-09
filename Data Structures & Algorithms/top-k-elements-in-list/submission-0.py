class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = defaultdict(int)
        res = []

        for num in nums:
            t[num] += 1
        
        for _ in range(k):
            mostfrq = max(t, key = t.get)
            res.append(mostfrq)
            t.pop(mostfrq)

        return res