class Solution:
    # Maximum k times
    # Return length of longest substring containing some letter
    # Constraints : There might exist other ways
    # 1 <= s.length <= 10^5
    # 0 <= k <= s.length

    # Algos : 
    # How to find the string has repeated char?
    # if sorted(sub) == sub , ABB ABB, NOT TRUE!
    # left, right pointers to look for 
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s)

        for c in charSet:
            count = l = 0 
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
            
        # for c in charSet:
        #     count = l = 0 
        #     for r in range(len(s)):
        #         if s[r] == c:
        #             count += 1

        #         while (r - l + 1) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1
        #         res = max(res, r - l + 1)
        # return res
