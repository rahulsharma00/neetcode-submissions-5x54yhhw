class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        nums = collections.Counter(nums)
        for k,v in nums.items():
            if v > n:
                return k
