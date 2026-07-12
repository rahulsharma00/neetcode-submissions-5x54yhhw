class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        out = []
        nums = collections.Counter(nums)
        for k,v in nums.items():
            if v > n:
                out.append(k)
        return out
