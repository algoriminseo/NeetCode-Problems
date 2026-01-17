class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for num in nums:
            freq[num] = 0 
        for num in nums:
            freq[num] += 1
  
        max_val = 0 
        max_key = 0 
        while k != 0:
            for key, value in freq.items():
                if value > max_val:
                    max_val = value
                    max_key = key
            res.append(max_key)
            freq[max_key] = 0
            max_val = 0 
            k -= 1
        return res