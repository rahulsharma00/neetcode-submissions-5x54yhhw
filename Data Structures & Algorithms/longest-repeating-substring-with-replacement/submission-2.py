class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l,maxFreq,ans = 0,0,0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])
            window = r-l+1
            replace = window - maxFreq
            if replace > k:
                count[s[l]] -=1 
                l +=1 
            ans = max(ans, r-l+1)
        return ans 