class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        count = 1
        longest = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue  
            elif nums[i + 1] == nums[i] + 1:
                count += 1  
            else:
                longest = max(longest, count)
                count = 1 
        return max(count, longest)