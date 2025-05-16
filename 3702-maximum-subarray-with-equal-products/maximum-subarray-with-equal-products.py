class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i:j+1]
                lcm = reduce(math.lcm, arr)
                gcd = reduce(math.gcd, arr)
                prod = math.prod(arr)
                if(prod == gcd * lcm):
                    result = max(result, j + 1 - i)
        return result
        