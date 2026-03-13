# Constraints:

# 1 <= nums1.length, nums2.length <= 9
# 1 <= nums1[i], nums2[i] <= 9
# All digits in each array are unique.

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    return num1
        
        res = min(nums1[0] * 10 + nums2[0], nums2[0] * 10 + nums1[0])
        return res
