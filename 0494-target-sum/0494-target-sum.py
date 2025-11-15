#Time Complexity : 
# Constraints:


# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1


        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count 

        return dp[n][target]