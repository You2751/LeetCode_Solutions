class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        
        for right in range(len(nums) - 1, -1, -1):
            left, mid = 0, right - 1
            while(left < mid):
                check_sum = nums[left] + nums[mid]
                if(check_sum > nums[right]):
                    result += mid - left
                    mid -= 1
                else:
                    left += 1
        return result