# Constraints:

# 1 <= n <= 20
# 1 <= k <= n

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sub = [], []

        def backtrack(i):
            if len(sub) == k:
                res.append(sub[:])
                return 

            for num in range(i, n + 1):
                sub.append(num)
                backtrack(num + 1)
                sub.pop()

        backtrack(1)
        return res

