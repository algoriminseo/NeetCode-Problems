# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = 1e9 
            for coin in coins:
                if amount - coin >= 0: 
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res

        minCoin = dfs(amount)
        return -1 if minCoin == 1e9 else minCoin 





