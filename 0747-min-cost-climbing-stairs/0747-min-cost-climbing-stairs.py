#Top to bottom : Top is last index + 1
# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# Time Complexity : O(n), where n is length of the array
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0] * (n + 1)


        for i in range(2, n + 1):
            res[i] = min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i -2])
        return res[n]