class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break

            l = i+1
            r = n-1
            a = nums[i]
            target = -a
            while l<r:
                total = nums[l]+nums[r]
                if target==total:
                    res.append([nums[i],nums[l],nums[r]])
                    left = nums[l]
                    right = nums[r]
                    while l<r and left == nums[l]:
                        l+=1
                    while l<r and right == nums[r]:
                        r-=1
                elif total<target:
                    l+=1
                else:
                    r-=1
            
        return res
