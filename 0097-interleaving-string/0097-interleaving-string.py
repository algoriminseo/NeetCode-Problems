class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Time Complexity : O(MN)
        if len(s1) + len(s2) != len(s3): 
            return False

        n1, n2 = len(s1), len(s2)

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True


        for i in range(1, n1 +1):
            for j in range(1, n2 + 1):
                if s2[i -1] == s3[i + j -1] and dp[i-1][j]:
                    dp[i][j] = True

                if s1[j - 1] == s3[i + j -1 ] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[n1][n2]
