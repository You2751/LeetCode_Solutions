class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = running_sum = left = 0
        counter = Counter(nums[:k])
        running_sum = sum(nums[:k])
        if(len(counter) == k):
            result = running_sum
        for right in range(k, len(nums)):
            counter[nums[right]] += 1
            counter[nums[right - k]] -= 1
            if(counter[nums[right - k]] == 0):
                del counter[nums[right - k]]
            running_sum += nums[right]
            running_sum -= nums[right - k]
            if(len(counter) == k):
                result = max(result, running_sum)
        return result