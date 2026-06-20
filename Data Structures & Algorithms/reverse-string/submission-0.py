class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b = len(s) - 1

        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[b]
            s[b] = t
            b += -1
            i += 1
            
        