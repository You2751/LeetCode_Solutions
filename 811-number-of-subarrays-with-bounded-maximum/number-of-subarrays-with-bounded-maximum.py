class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays(val):
            count = result = 0
            for num in nums:
                if(num <= val):
                    count += 1
                else:
                    count = 0
                result += count
            return result
        return count_subarrays(right) - count_subarrays(left - 1)