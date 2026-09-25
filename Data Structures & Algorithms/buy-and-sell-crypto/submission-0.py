class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you want a pair of values such that the later val - earlier val is maximized
        # move index forward, treating it as the sell; you want the minimum of all prior values
        
        max_val = 0

        for i, val in enumerate(prices):
            if val - min(prices[0:i], default=float('inf')) > max_val:
                max_val = val - min(prices[0:i])
        
        return max_val