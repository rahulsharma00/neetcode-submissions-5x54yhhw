class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf') # here is infinity so if we make res = 0 then min(res,r-l=1) will always be 0 since 0 is the smallest number and res won't update
        
        l = 0
        count = 0 
        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                res = min(res,r-l+1)
                count -= nums[l]
                l += 1
        return 0 if res == float('inf') else res 