class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())

        for c in range(len(s)):
            if not s[c].isalnum():
                s[c] = ""

        l, r = 0, len(s) - 1
        rev = [0] * len(s) # reversed

        while l <= r:
            tmp = s[l]
            rev[l] = s[r]
            rev[r] = tmp
            l += 1
            r -= 1
        
        return "".join(s) == "".join(rev)
