class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        c = 0 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(s[r])
            c = max(c,r-l+1)
        return c