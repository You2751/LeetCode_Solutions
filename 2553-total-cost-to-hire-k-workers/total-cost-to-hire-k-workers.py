class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        heap_left = costs[:candidates]
        heap_right = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(heap_left)
        heapq.heapify(heap_right)
        left_idx = candidates
        right_idx = len(costs) - candidates - 1
        for _ in range(k):
            condition = not heap_right or (heap_left and heap_left[0] <= heap_right[0])
            if(condition):
                total += heapq.heappop(heap_left)
                if(left_idx <= right_idx):
                    heapq.heappush(heap_left, costs[left_idx])
                    left_idx += 1
            else:
                total += heapq.heappop(heap_right)
                if(left_idx <= right_idx):
                    heapq.heappush(heap_right, costs[right_idx])
                    right_idx -= 1
        return total