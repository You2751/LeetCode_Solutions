class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if(len(nums) < k):
            return []
        counter = Counter(nums[:k])
        def get_total(counter):
            total = 0
            heap = [(-freq, -val) for val, freq in counter.items()]
            heapq.heapify(heap)
            for _ in range(x):
                if not heap:
                    break
                (freq, val) = heapq.heappop(heap)
                total += freq * val
            return total
        result = [get_total(counter)]
        for i in range(1, len(nums) - k + 1):
            out = nums[i - 1]
            counter[out] -= 1
            if(counter[out] <= 0):
                del counter[out]
            counter[nums[i + k - 1]] += 1
            result.append(get_total(counter))
        return result