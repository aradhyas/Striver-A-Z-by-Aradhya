class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        max_len = 0

        for x in s:
            if x-1 not in s:
                curr = x
                length = 1
                while curr+1 in s:
                    curr = curr+1
                    length = length+1
                max_len = max(length, max_len)
        return max_len