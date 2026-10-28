class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            
            else:
                freq[nums[i]] =1
        
            if freq[nums[i]] > len(nums)/2:
                return nums[i]

        