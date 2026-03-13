# Constraints:

# 1 <= nums1.length, nums2.length <= 9
# 1 <= nums1[i], nums2[i] <= 9
# All digits in each array are unique.

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)

        if common:
            return min(common)
        min1 = min(nums1)
        min2 = min(nums2)
        return min(10 * min1 + min2, 10 * min2 + min1)