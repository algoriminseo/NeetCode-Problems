# Constraints:
# Time : O(nlogn) Space : O(nlogn)
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)


        return minHeap[0]