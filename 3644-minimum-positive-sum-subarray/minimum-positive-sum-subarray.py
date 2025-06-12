class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        for idx in range(l, r + 1):
            left, right = 0, idx
            curr_sum = sum(nums[:idx])
            if(curr_sum > 0):
                result = min(result, curr_sum)
            while(right < len(nums)):
                curr_sum += nums[right]
                curr_sum -= nums[left]
                if(curr_sum > 0):
                    result = min(result, curr_sum)
                left += 1
                right += 1
        if(result != float('inf')):
            return result
        return -1