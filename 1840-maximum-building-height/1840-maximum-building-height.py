class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        
        for i in range(1, len(restrictions)):
            distance = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + distance)

        for i in range(len(restrictions) - 2, -1, -1):
            distance = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + distance)
        
        ans = 0
        for i in range(1, len(restrictions)):
            h1, h2 = restrictions[i-1][1], restrictions[i][1]
            distance = restrictions[i][0] - restrictions[i-1][0]
            peak = (h1 + h2 + distance) // 2
            ans = max(ans, peak)
        
        return ans