class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        min_heap = []

        for start, end in sorted_intervals:
            if(min_heap and min_heap[0] < start):
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)

        return len(min_heap) 