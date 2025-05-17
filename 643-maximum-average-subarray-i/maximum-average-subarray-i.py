class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(k == len(nums)):
            return sum(nums) / len(nums)
        curr_total = total = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_total -= nums[i - k]
            curr_total += nums[i]
            total = max(total,curr_total)
        return total / k