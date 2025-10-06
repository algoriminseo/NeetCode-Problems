# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, comb, total):
            if total == target:
                res.append(comb.copy())
                return 
            if i == len(candidates) or total > target:
                return 
            
            comb.append(candidates[i])
            dfs(i, comb, total + candidates[i])

            comb.pop()
            dfs(i + 1, comb, total)

        dfs(0, [], 0)
        return res 

       




