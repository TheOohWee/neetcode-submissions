class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r += -1
            return True

        r, l = len(s) - 1, 0
        while l < r:
            if s[l] != s[r]:
                return check(l, r - 1) or check(l + 1, r)
            l += 1
            r += -1
        return True
