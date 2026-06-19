class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = total_sum = 0 
        for i in range(len(gain)):
            total_sum+=gain[i]
            maxi = max(maxi, total_sum)
        
        return maxi