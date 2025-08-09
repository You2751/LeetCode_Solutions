class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        heap_left = costs[:candidates]
        heap_right = costs[max(candidates, len(costs) - candidates):]
        left_idx = candidates
        right_idx = len(costs) - candidates - 1
        heapq.heapify(heap_left)
        heapq.heapify(heap_right)
        for _ in range(k):
            if(not heap_right or (heap_left and heap_left[0] <= heap_right[0])):
                total_cost += heapq.heappop(heap_left)
                if(left_idx <= right_idx):
                    heapq.heappush(heap_left, costs[left_idx])
                    left_idx += 1
            else:
                total_cost += heapq.heappop(heap_right)
                if(left_idx <= right_idx):
                    heapq.heappush(heap_right, costs[right_idx])
                    right_idx -= 1
        return total_cost