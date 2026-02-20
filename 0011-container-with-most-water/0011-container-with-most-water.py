class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(height)-1
        while i<j:
            vol = (j-i) * min(height[i],height[j])
            max_vol = max(vol, max_vol)
            if height[i]<=height[j]:
                i+=1

            else:
                j-=1
        
        return max_vol