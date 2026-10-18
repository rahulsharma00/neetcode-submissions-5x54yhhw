class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {')':'(','}':'{',']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in mydict.values():
                stack.append(s[i])
            elif stack and stack[-1] == mydict[s[i]]:
                stack.pop()
            else:
                return False 
        return stack == []