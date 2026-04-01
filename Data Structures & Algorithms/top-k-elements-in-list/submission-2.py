class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        res = []

        while len(res) < k:
            max_key_value = max(count, key=count.get)
            res.append(max_key_value)

            del count[max_key_value]
        
        return res