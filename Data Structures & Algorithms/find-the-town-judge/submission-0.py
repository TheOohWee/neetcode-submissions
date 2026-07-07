class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        self.t = {} # n - 1

        for i in range(1, n + 1):
            # from 1 to 4 inclusive
            self.t.setdefault(i, 0)

        for i in trust:
            self.compare(i)
        
        for i in range(1, n + 1):
            if self.t[i] == n - 1:
                return i
        return -1


    def compare(self, pair):
        self.t[pair[0]] = self.t.get(pair[0]) - 1
        self.t[pair[1]] = self.t.get(pair[1]) + 1
        


