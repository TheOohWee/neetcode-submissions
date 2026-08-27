class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = defaultdict(int)
        r = []

        for i in range(len(arr)):
            d[i] = abs(arr[i] - x)

        for i in range(k):
            j = min(d, key=d.get)
            r.append(arr[j])
            d.pop(j)
            

        return sorted(r)

