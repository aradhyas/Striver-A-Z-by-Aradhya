class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        s = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = p
            p *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= s
            s *= nums[i]
        
        return result