class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for chars in strs:
            key = ''.join(sorted(chars))
            groups[key].append(chars)
        return list(groups.values())