class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split("/") # list
        stack = []

        for i in a:
            if i == "":
                pass
            elif i == ".":
                pass
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
