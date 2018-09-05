class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        if length <= 1:
            return profit
        for i in range(1, length):
            if prices[i] - prices[i - 1] >= 0:
                profit += prices[i] - prices[i - 1]

        return profit