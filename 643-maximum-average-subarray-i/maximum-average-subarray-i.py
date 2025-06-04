class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(len(nums) == k):
            return sum(nums) / k
        max_sum = curr_sum = sum(nums[:k])
        for right in range(k, len(nums)):
            curr_sum -= nums[right - k]
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
