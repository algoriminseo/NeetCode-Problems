# Time Complexity : O(n ^ 2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):   
                if LIS[i] < LIS[j]: 
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                continue

        return max(LIS)