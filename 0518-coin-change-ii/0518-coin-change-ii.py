# Constraints:

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n +1)]

        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            coin = coins[i - 1]

            for a in range(0, amount  + 1):
                dp[i][a] = dp[i-1][a]

                if a >= coin:
                    dp[i][a] += dp[i][a - coin]

        return dp[n][amount]

        