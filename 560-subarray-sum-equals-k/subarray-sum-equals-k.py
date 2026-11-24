class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        dic = defaultdict(int)
        dic[0] = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            result += dic[diff]
            dic[curr_sum] += 1
        return result