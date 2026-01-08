class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n + 1):
            tmp = 0 
            while i != 0:
                if i & 1 == 1:
                    tmp += 1
                i = i >> 1
            ans.append(tmp)

        return ans                
