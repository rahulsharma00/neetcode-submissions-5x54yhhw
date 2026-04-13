class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = collections.Counter(nums)
        res = []
        for k, v in count.items():
            if v > n / 3:
                res.append(k)
        return res