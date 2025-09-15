from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # absolute difference can't be negative

        nums.sort()
        n = len(nums)
        left, right = 0, 1
        count = 0

        while right < n:
            if left == right:
                right += 1
                continue

            diff = nums[right] - nums[left]

            if diff < k:
                # Need a larger difference → move right forward
                right += 1
            elif diff > k:
                # Difference too big → move left forward
                left += 1
            else:
                # Found a pair with difference k
                count += 1
                left += 1

                # Skip duplicates on the left so each pair value is counted once
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

                # Ensure right stays ahead
                if left >= right:
                    right = left + 1

        return count
