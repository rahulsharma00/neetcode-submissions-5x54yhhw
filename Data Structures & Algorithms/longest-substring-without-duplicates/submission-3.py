class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        count = 0 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            seen.add(s[right])
            count = max(count,right-left+1)
        return count

'''
# as long as there are no duplicates, left doesn't need to move 

while - because removing one character from the left might not be enough to remove duplicates 
eg s = abba 

if duplicate: remove one character
while duplicate: remove character(s)
'''