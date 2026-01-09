# Constraints:

# 0 <= n <= 231 - 2
# n is even.
class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = 0 

        for i in range(32):
            bit = (n >> i) & 1
            tmp |= bit << (31 - i) 
             
        return tmp
          
