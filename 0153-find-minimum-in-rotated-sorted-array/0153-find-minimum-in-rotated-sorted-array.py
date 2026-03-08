# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
# 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1


        while l < r:
            m = l + (r  - l ) // 2 
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        return nums[l]
















