class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        long = max(strs)
        small = min(strs)
        for i in range(len(small)):
            if small[i] == long[i]:
                output += small[i]
            else:
                break
        return output