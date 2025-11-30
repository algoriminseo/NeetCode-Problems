# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtrack(i):
            if i == len(nums):
                res.append(nums[:])
                return 
            
            seen = set()

            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue 

                seen.add(nums[j])
                
                nums[i], nums[j] = nums[j], nums[i]

                backtrack(i + 1)
            
                nums[j], nums[i] = nums[i], nums[j]

        backtrack(0)
    
        return res
            
