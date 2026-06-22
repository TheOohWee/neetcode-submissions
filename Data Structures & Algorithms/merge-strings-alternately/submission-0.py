class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1) and i < len(word2):
                new += word1[i]# add(word1, i)
                new += word2[i]# add(word2, i)
                i += 1
            elif i < len(word1):
                new += word1[i]
                i += 1
            elif i < len(word2):
                new += word2[i]
                i += 1

        return new