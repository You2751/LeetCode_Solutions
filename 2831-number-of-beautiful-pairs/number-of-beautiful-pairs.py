from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                first_digit = str(nums[i])[0]
                last_digit = str(nums[j])[-1]
                if(math.gcd(int(first_digit), int(last_digit)) == 1):
                    pairs += 1
        return pairs
