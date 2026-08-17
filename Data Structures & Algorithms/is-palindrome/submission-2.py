class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = re.sub(r'[^a-zA-Z0-9]+', '', s)
        w = w.lower()
        l,r = 0,len(w)-1
        while l < r:
            if w[l] == w[r]:
                l += 1
                r -= 1
            else:
                return False 
        return True 