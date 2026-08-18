class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            L, R = 0, len(s1)

            while L < R:
                if sorted(s1) == sorted(s2[L:R]):
                    return True
                else:
                    if R < len(s2):
                        R += 1
                    if L < len(s2):
                        L += 1
        return False
        
