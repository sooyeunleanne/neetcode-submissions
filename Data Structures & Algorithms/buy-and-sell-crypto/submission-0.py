class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_so_far)
            min_so_far = min(min_so_far, price)

        return max_profit
