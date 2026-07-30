class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        x = len(nums)//2
        for k,v in nums.items():
            if v > x:
                return k