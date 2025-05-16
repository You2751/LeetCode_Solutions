class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_val = result = float('-inf')
        overall_lcm = 1

        for num in nums:
            max_val = max(max_val, num)
            overall_lcm = math.lcm(overall_lcm, num)
        max_all = overall_lcm * max_val

        for i in range(len(nums)):
            prod, gcd, lcm = 1, 0, 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = math.lcm(lcm, nums[j])
                if(prod == lcm * gcd):
                    result = max(result, j - i + 1)

        return result