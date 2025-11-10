from bisect import bisect_left
# Time Complexity : O(n ^ 2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1 
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            index = bisect_left(dp, nums[i])
            dp[index] = nums[i]
        return LIS