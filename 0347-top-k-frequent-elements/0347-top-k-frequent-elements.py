class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        
        sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse=True)

        res = []
        for num,count in sorted_items[:k]:
            res.append(num)
        
        return res