class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = [] # "4#neet4#code"
        i = 0 # Postion we're at in input string

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) 
    # Tells us how many chars we have to read after j in order to get every character of the string 
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
                