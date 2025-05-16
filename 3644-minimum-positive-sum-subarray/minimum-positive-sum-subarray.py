class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        for i in range(l, r + 1):
            curr_sum = sum(nums[:i])
            if(curr_sum > 0):
                result = min(result, curr_sum)
            low, high = 0, i
            while(high < len(nums)):
                curr_sum -= nums[low]
                curr_sum += nums[high]
                low += 1
                high += 1
                if(curr_sum > 0):
                    result = min(result, curr_sum)
        return result if result != float('inf') else -1