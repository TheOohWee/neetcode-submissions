class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.d = {}

        for i in range(len(order)):
            self.d.setdefault(order[i], i)

        for i in range(len(words) - 1):
            if not self.compare(words[i], words[i+1]):
                return False

        return True


    def compare(self, a, b):
        for i in range(min(len(a), len(b))):
            if self.d.get(a[i]) < self.d.get(b[i]):
                return True
            if self.d.get(a[i]) == self.d.get(b[i]):
                continue
            if self.d.get(a[i]) > self.d.get(b[i]):
                return False     
                           
        return len(a) <= len(b)
        return False