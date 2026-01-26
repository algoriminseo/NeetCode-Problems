class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

     
        for i, num in enumerate(nums):
            num2 = target - num 
            if num2 in prev_map:
                return [prev_map[num2], i]
            prev_map[num] = i 