class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = left = 0
        max_heap, min_heap = [], []
        for right, val in enumerate(nums):
            heapq.heappush(max_heap, (-val, right))
            heapq.heappush(min_heap, (val, right))
            while(-max_heap[0][0] - min_heap[0][0] > limit):
                left += 1
                while(min_heap and min_heap[0][1] < left):
                    heapq.heappop(min_heap)
                while(max_heap and max_heap[0][1] < left):
                    heapq.heappop(max_heap)
            result = max(result, right - left + 1)
        return result