
# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

# make distance value as minimum val 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        dist_Map = {}

        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(minHeap, (distance, x, y))
        while k:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res