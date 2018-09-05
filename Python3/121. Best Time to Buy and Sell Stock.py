class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPrice = 0
        length = len(prices)
        if length <= 1:
            return maxPrice
        cur = prices[0]
        for i in range(1, length):
            if prices[i] - cur < 0:
                cur = prices[i]
            elif prices[i] - cur > maxPrice:
                maxPrice = prices[i] - cur

        return maxPrice