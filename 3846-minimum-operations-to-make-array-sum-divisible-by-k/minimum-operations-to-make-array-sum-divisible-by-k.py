class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if(total % k == 0):
            return 0
        steps = 0
        while(total % k):
            total -= 1
            steps += 1
        else:
            return steps