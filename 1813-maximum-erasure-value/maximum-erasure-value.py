class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        check = set()
        result = running_sum = left = 0
        for right, num in enumerate(nums):
            while(num in check):
                running_sum -= nums[left]
                check.remove(nums[left])
                left += 1
            running_sum += num
            result = max(result, running_sum)
            check.add(num)
        return result