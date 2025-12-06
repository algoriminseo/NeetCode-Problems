# Constraints:
# 2 <= k <= 9
# 1 <= n <= 60
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        res, seq = [], []
        
        def dfs(j, total):
            if len(seq) == k and total == n:
                res.append(seq.copy())
                return
    
            if j >= 9 or total > n:
                return 
            
            
            seq.append(nums[j])    
            dfs(j + 1, total + nums[j])

            seq.pop()
            dfs(j + 1, total)
        dfs(0, 0)
        return res