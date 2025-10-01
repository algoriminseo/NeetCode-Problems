# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
   
    def helper(self, nums): 
        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n + 1]
        for i in range(len(nums)):
            tmp = max(nums[i] + rob1, rob2)
            rob1 = rob2 
            rob2 = tmp
        return rob2