class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        result = 0
        running_sum = sum(nums[:k])
        counter = Counter(nums[:k])
        if(len(counter) >= m):
            result = running_sum = sum(nums[:k])
        print(result)
        for right in range(k, len(nums)):
            counter[nums[right]] += 1
            counter[nums[right - k]] -= 1
            if(counter[nums[right - k]] == 0):
                del counter[nums[right - k]]
            running_sum += nums[right]
            running_sum -= nums[right - k]
            if(len(counter) >= m):
                result = max(result, running_sum)
        return result