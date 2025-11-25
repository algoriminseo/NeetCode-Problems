# Constraints:

# 1 <= nums.length <= 105
# -10^4 <= nums[i] <= 10^4

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = float('-inf')
        curr_sum = 0 
       
        for num in nums:
            curr_sum += num 
            total_max = max(total_max, curr_sum)
            if curr_sum < 0:
                curr_sum = 0 
        

        return total_max

            

            


    
