class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2,can1,can2 = 0,0,None,None
        n = len(nums)
        if not nums:
            return []
        for num in nums:
            if can1 == num:
                count1 += 1
            elif can2 == num:
                count2 += 1
            elif count1 == 0:
                can1 = num
                count1 += 1
            elif count2 == 0:
                can2 = num
                count2 += 1
            else:
                count1 -=1 
                count2 -=1 
            
        res = []
        for c in [can1,can2]:
            if nums.count(c) > n//3:
                res.append(c)
        return res