class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        if(k > min_val):
            return -1
        counter = Counter(nums)
        if(k in counter):
            return len(counter) - 1
        return len(counter)