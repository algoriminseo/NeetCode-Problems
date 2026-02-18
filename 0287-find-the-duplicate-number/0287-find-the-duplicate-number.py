# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

        
