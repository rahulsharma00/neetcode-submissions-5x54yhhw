class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l = 0
        max_freq = 0
        answer = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            window = r - l + 1
            replacements = window - max_freq
            if replacements > k:
                count[s[l]] -= 1
                l += 1
            answer = max(answer, r - l + 1)
        return answer