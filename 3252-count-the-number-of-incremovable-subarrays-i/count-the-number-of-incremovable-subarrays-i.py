class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0                       # safety, though n ≥ 1 on LeetCode

        # 1) longest strictly-increasing prefix
        prefix_end = 1
        while prefix_end < n and nums[prefix_end] > nums[prefix_end - 1]:
            prefix_end += 1

        # 2) already strictly increasing?  all non-empty subarrays work
        if prefix_end == n:
            return n * (n + 1) // 2

        # 3) longest strictly-increasing suffix
        suffix_start = n - 1
        while suffix_start > 0 and nums[suffix_start] > nums[suffix_start - 1]:
            suffix_start -= 1

        ans = 0

        # 4a) remove-suffix cases  ── cut from s to end,  s ∈ [1 .. prefix_end]
        ans += prefix_end                       #  exactly prefix_end choices

        # 4b) remove-prefix cases  ── cut 0..p,   p ∈ [suffix_start-1 .. n-1]
        ans += n - suffix_start + 1             #  +1 counts “delete whole array”

        # 4c) remove-middle cases:     keep a prefix ending at i (0 ≤ i < prefix_end)
        #                              keep a suffix starting at j (suffix_start ≤ j < n)
        #                              and need nums[i] < nums[j]
        i = 0
        j = suffix_start
        while i < prefix_end:
            while j < n and nums[j] <= nums[i]:
                j += 1
            ans += n - j                        # every k ≥ j is valid for this i
            i += 1

        return ans