class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = False)
        for i in range(len(nums) + 1):
            if i in nums:
                continue
            return i 

