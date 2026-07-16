class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0:1}
        for n in nums:
            prefix+=n
            check = prefix - k
            if check in seen:
                count += seen[check]
            
            if prefix in seen:
                seen[prefix] = seen[prefix] + 1
            else:
                seen[prefix] = 1

        return count