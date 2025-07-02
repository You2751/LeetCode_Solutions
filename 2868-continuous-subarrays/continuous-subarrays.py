class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_heap = []
        min_heap = []
        result = left = 0
        for right, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, right))
            heapq.heappush(min_heap, (num, right))
            while(-max_heap[0][0] - min_heap[0][0] > 2):
                left += 1
                while(max_heap[0][1] < left):
                    heapq.heappop(max_heap)
                while(min_heap[0][1] < left):
                    heapq.heappop(min_heap)
            result += right - left + 1
        return result