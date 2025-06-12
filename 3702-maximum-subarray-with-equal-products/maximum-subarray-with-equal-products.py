class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = float('-inf')
        for left in range(len(nums)):
            gcd, lcm, prod = 0, 1, 1
            for right in range(left, len(nums)):
                prod *= nums[right]
                gcd = math.gcd(gcd, nums[right])
                lcm = math.lcm(lcm, nums[right])
                if(prod == lcm * gcd):
                    result = max(result, right - left + 1)
        return result