class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = ""

        for i in range(len(s)):
            if s[i] == "[":
                stack.append((cur, num))
                cur = ""
                num = ""
            elif s[i].isdigit():
                num += s[i]   
            elif s[i] == "]":
                prevs, prevn = stack.pop()
                expanded = cur * int(prevn)
                cur = prevs + expanded
            else:
                cur += s[i]
            
        return cur