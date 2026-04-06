class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        res = []

        for i in range(k):
            max_key = max(count, key=count.get)
            res.append(max_key)
            del count[max_key]
        return res