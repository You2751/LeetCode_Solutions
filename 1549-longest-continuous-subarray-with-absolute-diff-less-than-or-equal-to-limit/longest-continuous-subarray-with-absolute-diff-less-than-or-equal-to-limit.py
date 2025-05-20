class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []
        left = result = 0
        for right, val in enumerate(nums):
            heapq.heappush(max_heap, (-val, right))
            heapq.heappush(min_heap, (val, right))

            while(-max_heap[0][0] - min_heap[0][0] > limit):
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                while(max_heap[0][1] < left):
                    heapq.heappop(max_heap)
                while(min_heap[0][1] < left):
                    heapq.heappop(min_heap)
            result = max(result, right - left + 1)
        return result