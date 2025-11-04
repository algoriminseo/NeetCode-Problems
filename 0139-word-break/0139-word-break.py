# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if ((i + len(word)) <= len(s) and s[i : i + len(word)] == word):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False
        
        return dfs(0)



     








        