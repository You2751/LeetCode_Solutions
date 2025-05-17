class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        result = float('-inf')
        for left in range(len(nums)):
            right = left
            while(right < len(nums) and abs(nums[left] - nums[right]) <= min(nums[left], nums[right])):
                result = max(result, nums[left] ^ nums[right])
                right += 1
        return result