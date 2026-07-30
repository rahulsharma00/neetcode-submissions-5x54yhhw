class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for char in strs:
            key = ''.join(sorted(char))
            res[key].append(char)
        return list(res.values())