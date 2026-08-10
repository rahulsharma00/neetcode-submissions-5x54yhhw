class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + '#' + i
        return res
        # 4#Hello5#World
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:length + j + 1])
            i = length + j + 1
        return res

