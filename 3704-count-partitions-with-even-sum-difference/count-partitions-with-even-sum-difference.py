class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0
        left_sum = 0
        right_sum = sum(nums)
        for num in nums:
            left_sum += num
            right_sum -= num
            if(right_sum == 0):
                break
            diff = abs(left_sum - right_sum)
            if(diff % 2 == 0):
                result += 1
        return result