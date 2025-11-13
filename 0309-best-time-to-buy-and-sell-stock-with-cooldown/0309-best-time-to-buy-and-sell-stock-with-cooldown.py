# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        hold, sold, rest = [0] * n, [0] * n, [0] * n
        hold[0], sold[0], rest[0] = -prices[0], 0, 0 

        for i in range(1, n):

            hold[i] = max(hold[i-1], rest[i-1] - prices[i])

            sold[i] = hold[i-1] + prices[i]

            rest[i] = max(rest[i-1], sold[i-1])

        return max(rest[n-1], sold[n-1])