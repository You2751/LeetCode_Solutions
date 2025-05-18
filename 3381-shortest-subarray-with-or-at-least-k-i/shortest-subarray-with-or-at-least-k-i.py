class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = float('inf')
        for left in range(len(nums)):
            curr = 0
            for right in range(left, len(nums)):
                curr |= nums[right]
                if(curr >= k):
                    result = min(result, right - left + 1)
                    break
        return result if result != float('inf') else -1