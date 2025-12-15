# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda pair : pair[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = intervals[-1][1]
            if start <= lastEnd:
               res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])        
        return res