from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        new_length = length//2
        c = dict(Counter(nums))
        for k,v in c.items():
            if v > new_length:
                return k
            