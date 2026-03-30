class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        p = 0
        max_profit = 0

        for r in range(1,len(prices)):
            if prices[r] > prices[p]:
                max_profit = max(max_profit,prices[r] - prices[p])
            if prices[r] < prices[p]:
                p = r
        
        return max_profit