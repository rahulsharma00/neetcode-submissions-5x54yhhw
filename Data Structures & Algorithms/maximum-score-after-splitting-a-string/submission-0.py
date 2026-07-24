class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        c = 0 
        for i in range(1,len(s)):
            l,r = s[:i], s[i:]
            score = l.count('0') + r.count('1')
            c = max(c,score)
        return c