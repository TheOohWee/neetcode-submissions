class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        window = deque()
        count = defaultdict(int)
        mfrq = 0

        for R in range(len(s)):
            count[s[R]] += 1 
            mfrq = max(mfrq, count[s[R]])
            while len(window) - mfrq >= k:
                a = window.popleft()
                count[a] -= 1
                L += 1

            window.append(s[R])
            max_len = max(max_len, R - L + 1)

        return max_len