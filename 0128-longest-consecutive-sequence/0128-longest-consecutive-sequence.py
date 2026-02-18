class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        count = 0
        maxlength = 0
        for i in num:
            if i-1 not in num:
                curr = i
                count=1
                while curr+1 in num:
                    curr = curr+1
                    count+=1
                
                maxlength = max(count, maxlength)
        return maxlength