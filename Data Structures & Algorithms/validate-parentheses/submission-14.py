class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d[')'] = '('
        d['}'] = '{'
        d[']'] = '['

        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in d:
                if stack and stack[-1] == d[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
