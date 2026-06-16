class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for j in range(len(strs[0])):
            c = strs[0][j] 
            for word in strs:
                if j >= len(word) or word[j] != c:
                    return pref
            pref += c
        return pref
            
            