class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        min_val = float('inf')
        max_product = max_val = float('-inf')

        for end in range(m - 1, len(nums)):
            end_val = nums[end]
            start_val = nums[end - (m - 1)]

            min_val = min(min_val , start_val)
            max_val = max(max_val, start_val)

            max_product = max(max_product, end_val * min_val, end_val * max_val)
        return max_product