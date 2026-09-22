class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        l = 0 
        seen = set()
        maxf = 0
        count = Counter() 
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf,count[s[r]])
            window = r-l+1
            replace = window - maxf
            if replace > k:
                count[s[l]] -= 1
                l +=1 
            ans = r-l+1
        return ans 