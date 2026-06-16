class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = {} # dict to compare
        t_hm = {}

        # checking before algo
        if len(s) != len(t):
            return False
        else: 
        #algo
            for i in s:
                s_hm[i] = s_hm.get(i, 0) + 1
            for j in t:
                t_hm[j] = t_hm.get(j, 0) + 1
        if t_hm == s_hm:
            return True
        else: 
            return False


                
                    