# Constraints:

# 1 <= nums.length <= 105
# -10^4 <= nums[i] <= 10^4

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = nums[0], 0 
       
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0 
            curr_sum += num 
            max_sum = max(curr_sum, max_sum)

        return max_sum 

            

            


    
