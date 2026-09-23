class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False 

        window = Counter(s1)
        count = Counter()
        l = 0
        for r in range(len(s2)):
            count[s2[r]] += 1 # this is adding individial chars in count so for eg count = {l:1,e:1}
            if r-l+1>len(s1): # once done being added, it's checking if the length of chars in the current window > len(s1)
                count[s2[l]] -=1 # if this is true then we remove one char since both the legth of count and window needs to be the same 
                l +=1 
            if count == window: # once removed we check if the chars are same in both and return True if else else False 
                return True 
        return False         
