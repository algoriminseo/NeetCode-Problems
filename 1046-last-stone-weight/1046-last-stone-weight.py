# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# x <= y
#Time Complexity : O(nlogn) Space Complexity : O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) >= 2:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if x == y:
                continue
            else:
                y = y - x
                heapq.heappush(maxHeap,-y)
        if len(maxHeap) == 1:
            return -maxHeap[0]
        return 0
