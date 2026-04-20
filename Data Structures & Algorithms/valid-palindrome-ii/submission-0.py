class Solution:
    def isPalindrome(self, s: str,left,right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False 
            left += 1 
            right -=1 
        return True 

    def validPalindrome(self,s):
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s,left+1,right) or self.isPalindrome(s,left,right-1)
            left += 1
            right -= 1
        return True 