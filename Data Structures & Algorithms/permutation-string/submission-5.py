class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            L, R = 0, len(s1) - 1
            need = defaultdict(int)
            window = defaultdict(int)

            for i in s1:
                need[i] += 1

            for i in s2[L:R+1]:
                window[i] += 1

            if L == R and need == window: 
                return True
            
            while L < R:
                if need == window:
                    return True
                if L < len(s2) - 1:
                    window[s2[L]] -= 1
                    if window[s2[L]] == 0:
                        window.pop(s2[L])
                    L += 1
                if R < len(s2) - 1:
                    R += 1
                    window[s2[R]] += 1

        return False