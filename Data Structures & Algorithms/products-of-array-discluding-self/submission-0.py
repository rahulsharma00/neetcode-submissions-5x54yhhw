class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range((n)-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output 


        # [1,2,3,4]
        # prefix - [1,2,3,4] - 1,1,2,6
        # suffix - [4,3,2,1] - 24,12,4,1
