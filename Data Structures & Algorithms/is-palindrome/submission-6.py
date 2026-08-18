class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for chars in s:
            if chars.isalnum():
                res += chars
        res = res.lower()
        return res == res[::-1]