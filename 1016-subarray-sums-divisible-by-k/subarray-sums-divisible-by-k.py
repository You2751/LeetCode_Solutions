class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        result = curr_sum = 0
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k 
            result += prefix[remainder]
            prefix[remainder] += 1
        return result