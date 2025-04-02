class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can_reduce(mid):
            carry = 0
            for i in range(len(nums) - 1, 0, -1):
                total = nums[i] + carry
                if(total > mid):
                    carry = total - mid
                else:
                    carry = 0
            return nums[0] + carry <= mid
        left, right = 0, max(nums)
        while(left <= right):
            mid = (left + right) >> 1
            if(can_reduce(mid)):
                right = mid - 1
            else:
                left = mid + 1
        return left