class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []

        for stone in stones:
            heapq.heappush(self.heap, -stone)

        while len(self.heap) >= 2:     
            first = -heapq.heappop(self.heap)
            second = -heapq.heappop(self.heap)
            if first > second:
                heapq.heappush(self.heap, second - first)
            elif first == second:
                pass
            elif second > first:
                heapq.heappush(self.heap, first - second)

        if len(self.heap) == 1:
            return -self.heap[0]
        else:
            return 0


