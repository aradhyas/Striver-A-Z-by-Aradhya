import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        maxi = max(piles)
        while k<maxi:
            mid = (k+maxi)//2
            hour = 0
            for pile in piles:
                hour+=math.ceil(pile/mid)
            
            if hour<=h:
                maxi = mid
            
            else:
                k=mid+1
            
        
        return k
            


