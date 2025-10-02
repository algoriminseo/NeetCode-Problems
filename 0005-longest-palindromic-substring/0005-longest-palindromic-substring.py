# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_index = 0
        res_len = 0 

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l +1) > res_len:
                    res_index = l
                    res_len = r - l + 1
                l -= 1
                r += 1
            
            l, r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l +1) > res_len:
                    res_index = l
                    res_len = r - l + 1
                l -= 1
                r += 1

        return s[res_index :res_index + res_len]
