class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i: j + 1]
                gcd = reduce(math.gcd, arr)
                lcm = reduce(math.lcm, arr)
                prod = math.prod(arr)
                if(prod == lcm * gcd):
                    result = max(result, j - i + 1)
        return result