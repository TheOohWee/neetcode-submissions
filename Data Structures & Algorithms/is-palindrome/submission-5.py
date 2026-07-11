class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join((c for c in s if c.isalnum()))
        filtered = filtered.lower()

        return filtered == filtered[::-1]