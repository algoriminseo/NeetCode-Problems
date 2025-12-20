# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
          

            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

