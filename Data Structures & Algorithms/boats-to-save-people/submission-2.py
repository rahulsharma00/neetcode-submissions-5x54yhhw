class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        count = 0
        p.sort()
        l,r = 0, len(p)-1
        while l <= r:
            if p[l] + p[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count += 1
        return count