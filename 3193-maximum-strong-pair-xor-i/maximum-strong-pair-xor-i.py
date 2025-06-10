class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if(abs(nums[left] - nums[right]) <= min(nums[left], nums[right])):
                    result = max(result, nums[left] ^ nums[right])
                else:
                    break
        return result
