class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            nums2 = target - num

            if nums2 in prev_map:
                return [prev_map[nums2], i]


            prev_map[num] = i 