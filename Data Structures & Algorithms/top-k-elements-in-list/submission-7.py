class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        out = []
        for i in range(k):
            max_key = max(count, key=count.get)
            out.append(max_key)
            del count[max_key]
        return out
