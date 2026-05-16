import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = sys.maxsize
        low = high = 0
        total = 0
        while high<len(nums):
            total = nums[high] + total
            while total>=target:
                length = high-low+1
                res = min(length, res)
                total = total - nums[low]
                low+=1
            high+=1
        return 0 if res == sys.maxsize else res