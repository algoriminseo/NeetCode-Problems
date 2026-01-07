# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_result = 0 

        for num in nums:
            xor_result = xor_result * num

        
        return xor_result
