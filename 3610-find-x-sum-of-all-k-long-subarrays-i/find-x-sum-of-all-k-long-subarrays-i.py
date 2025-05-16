class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if(len(nums) < k):
            return []
        counter = Counter(nums[:k])
        def calculate_sum(counter):
            heap = [(-freq, -val) for val, freq in counter.items()]
            heapq.heapify(heap)
            total = 0
            for _ in range(x):
                if not heap:
                    break
                freq, val = heapq.heappop(heap)
                freq, val = -freq, -val
                total += (freq * val)
            return total
        result = [calculate_sum(counter)]
        for i in range(1, len(nums) - k + 1):
            out_val = nums[i - 1]
            counter[out_val] -= 1
            if(counter[out_val] <= 0):
                del counter[out_val]
            in_val = nums[i + k - 1]
            counter[in_val] += 1
            result.append(calculate_sum(counter))
        return result