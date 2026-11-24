class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        result = 0
        dic = defaultdict(int)
        dic[0] = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k 
            result += dic[remainder]
            dic[remainder] += 1
        return result