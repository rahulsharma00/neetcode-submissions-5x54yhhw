class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2,can1,can2 = 0,0,None,None
        res = []
        length = len(nums)
        if not nums:
            return []
        for n in nums:
            if can1 == n:
                count1 += 1
            elif can2 == n:
                count2 += 1
            elif count1 == 0:
                can1 = n
                count1 +=1
            elif count2 == 0:
                can2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -=1 

        return [c for c in [can1,can2] if nums.count(c) > length//3]