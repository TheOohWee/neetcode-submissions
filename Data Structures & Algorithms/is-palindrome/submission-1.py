class Solution:
    def isPalindrome(self, s: str) -> bool:

        w = s.lower().replace(" ", "")
        table = w.maketrans("", "", "!@#$%^&*()_-?/|\{}[],.`~:;'<>")
        w = w.translate(table)

        a = 0
        b = len(w) - 1

        while b >= a:
            if w[a] == w[b]:
                b += -1
                a += 1
                continue
            else:
                return False

        return True   
