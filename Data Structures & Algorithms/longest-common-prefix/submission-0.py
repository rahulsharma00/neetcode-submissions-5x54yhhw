class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = min(strs)
        b = max(strs)
        output = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                output += a[i]
            else:
                break
        return output