class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        total = 0
        counter = Counter(nums)
        for num, count in counter.items():
            if(count % k == 0):
                total += num * count
        return total