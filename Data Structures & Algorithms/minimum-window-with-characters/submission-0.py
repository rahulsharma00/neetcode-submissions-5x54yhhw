class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        window = Counter()

        l = 0
        have = 0
        need = len(count)

        res = ""
        resLen = float('inf')

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1

                l += 1

        return res