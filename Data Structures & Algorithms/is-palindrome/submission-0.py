class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''
        for char in s:
            if char.isalnum():
                r += char
        r = r.lower()
        return r == r[::-1]