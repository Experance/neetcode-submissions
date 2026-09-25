class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers, the start one points at the one that you buy at, end the one that you sell at, and save
        # max value in between (sell - buy) 
        # We update max_val when the sell > buy, and when sell < buy, we update the buy day to that sell day,
        # because it will be cheaper then

        buy = 0
        sell = 1
        max_val = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                # make profit, check max_val
                max_val = max(max_val, prices[sell] - prices[buy])
                # shift sell day
                sell += 1
            else:
                # no profit, update buy day
                buy = sell
                sell += 1

        return max_val
