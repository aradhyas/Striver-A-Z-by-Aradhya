# class Solution:
#     def maxTotalValue(self, nums: List[int], k: int) -> int:
#         values = []
#         for r in range(len(nums)):
#             current_max = nums[r]  # subarray starts as just [r]
#             current_min = nums[r]
        
#             for l in range(r, -1, -1):
#                 current_max = max(current_max, nums[l])
#                 current_min = min(current_min, nums[l])
#                 value = current_max - current_min
#                 values.append(value)
        
#         values.sort(reverse=True)

#         return sum(values[0:k])
        # values = []
    
        # for r in range(len(nums)):
        #     for l in range(r, -1, -1):
        #         value = max(nums[l:r+1]) - min(nums[l:r+1])
        #         values.append(value)
        
        # values.sort(reverse=True)

        # return sum(values[0:k])
# import heapq

# class Solution:
#     def maxTotalValue(self, nums: List[int], k: int) -> int:
#         heap = []
        
#         for r in range(len(nums)):
#             current_max = nums[r]
#             current_min = nums[r]
            
#             for l in range(r, -1, -1):
#                 current_max = max(current_max, nums[l])
#                 current_min = min(current_min, nums[l])
#                 value = current_max - current_min
#                 heapq.heappush(heap, value)      
#                 if len(heap) > k:
#                     heapq.heappop(heap)  
        
#         return sum(heap)
# import heapq

# class Solution:
#     def maxTotalValue(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         heap = []
        
#         # push best value from each row
#         for r in range(n):
#             val = max(nums[0:r+1]) - min(nums[0:r+1])
#             heapq.heappush(heap, (-val, r, 0))  # negative because min heap
        
#         answer = 0
#         for _ in range(k):
#             val, r, l = heapq.heappop(heap)
#             answer += -val  # convert back to positive
            
#             if l + 1 <= r:  # still more candidates in this row
#                 new_val = max(nums[l+1:r+1]) - min(nums[l+1:r+1])
#                 heapq.heappush(heap, (-new_val, r, l+1))
        
#         return answer

import heapq
import math

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = max(1, math.floor(math.log2(n)) + 1)
        
        # build sparse table for range max and range min
        # sparse_max[j][i] = max of nums[i .. i + 2^j - 1]
        sparse_max = [[0] * n for _ in range(LOG)]
        sparse_min = [[0] * n for _ in range(LOG)]
        
        for i in range(n):
            sparse_max[0][i] = nums[i]
            sparse_min[0][i] = nums[i]
        
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                sparse_max[j][i] = max(sparse_max[j-1][i], sparse_max[j-1][i + (1 << (j-1))])
                sparse_min[j][i] = min(sparse_min[j-1][i], sparse_min[j-1][i + (1 << (j-1))])
        
        def query(l, r):
            length = r - l + 1
            j = math.floor(math.log2(length))
            mx = max(sparse_max[j][l], sparse_max[j][r - (1 << j) + 1])
            mn = min(sparse_min[j][l], sparse_min[j][r - (1 << j) + 1])
            return mx - mn
        
        # heap: (-value, l, r)
        # start with widest subarray for each l (r = n-1)
        heap = []
        for l in range(n):
            val = query(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))
        
        answer = 0
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            answer += -val
            
            if r - 1 >= l:  # shrink from right
                new_val = query(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))
        
        return answer