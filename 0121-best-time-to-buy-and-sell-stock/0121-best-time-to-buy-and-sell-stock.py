#Constraints:
#1 <= prices.length <= 10^5
#0 <= prices[i] <= 10^4


# Algo : use left and right pointers
# Iterate through one and other, move right and go 
# Reverse order -> cannot achive profit 
#Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_price = 0 
        
        while right < len(prices):
            if prices[left] < prices[right]:
                max_price = max(max_price, prices[right] - prices[left])

            else:
                left = right

            right += 1
        return max_price 