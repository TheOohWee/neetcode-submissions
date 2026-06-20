class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # new array reversed
        new = []

        for i in range(len(s)):
            new.append(s[len(s) - 1 - i])

        for i in range(len(s)):
            s[i] = new[i]