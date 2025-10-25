#Time Complexity : O(n)
#Space Compelxity : O(`1)

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0 
        n = len(s)  
        dp = [[False] * n for u in range(n)] 


        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = (j - i + 1)

        return s[resIdx : resIdx + resLen]


