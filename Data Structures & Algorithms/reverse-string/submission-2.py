class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # recursion = base case + return function
        self.s = s
        l = 0
        r = len(s) - 1

        def reverse(l: int, r: int) -> None:            
            #base case
            if l >= r:
                return s
            
            #recursive function
            t = s[l]
            s[l] = s[r]
            s[r] = t
            reverse(l + 1, r - 1)

        reverse(l, r)

            