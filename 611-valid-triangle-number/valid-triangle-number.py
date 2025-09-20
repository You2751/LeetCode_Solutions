class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for k in range(len(nums) -1, -1, -1):
            left, right = 0, k - 1
            while(left < right):
                check_sum = nums[left] + nums[right]
                if(check_sum > nums[k]):
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result

