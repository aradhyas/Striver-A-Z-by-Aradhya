class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        mincost = prices[0]

        for i in range(1, len(prices)):
            if mincost>prices[i]:
                mincost = prices[i]
            
            else:
                profit = max(profit, prices[i]-mincost)
        
        return profit
            
