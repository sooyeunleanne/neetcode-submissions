class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = float('inf')

        for i in range(len(prices)):
            lowest = min(prices[i], lowest)

            max_profit = max(prices[i] - lowest, max_profit)

        return max_profit