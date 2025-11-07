# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]





     








        