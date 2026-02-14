class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        seen = {}
        for i,x in enumerate(nums):
            other = target - x
            if other in seen:
                return [seen[other],i]
            seen[x] = i