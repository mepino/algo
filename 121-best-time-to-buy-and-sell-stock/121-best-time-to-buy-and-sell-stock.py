import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        historical_min_val = np.inf

        for i in range(len(prices)-1):
            if (i == 0) or (prices[i] < historical_min_val):
                buy = prices[i]
                historical_min_val = prices[i]
                
                sell = max(prices[i+1:])
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit
            else:
                continue
        return max_profit