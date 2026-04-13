class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0  
        maxProfit = 0 

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
                maxProfit = profit if profit > maxProfit else maxProfit
            else:
                left = right
            right += 1
        
        return maxProfit