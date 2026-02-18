class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr = 0
        l = 0
        r = len(numbers)-1
        while l<r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l + 1, r + 1]
            
            if curr<target:
                l+=1
                continue
            else:
                r-=1
                continue
        
        return []