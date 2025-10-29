# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []
        subset = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            dfs(i + 1 , subset)

        dfs(0, subset)

        return res