class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)
        window = (2 * k) + 1
        if(window > len(nums)):
            return result
        running_sum =  sum(nums[:window])
        result[k] = running_sum // window
        for i in range(k + 1, len(nums) - k):
            running_sum -= nums[i - k - 1]
            running_sum += nums[i + k]
            result[i] = running_sum // window
        return result