class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(changes):
            left = result = 0
            for right in range(len(nums)):
                changes -= nums[right] % 2
                while(changes < 0):
                    changes += nums[left] % 2
                    left += 1
                result += right - left + 1
            return result
        return at_most(k) - at_most(k - 1)