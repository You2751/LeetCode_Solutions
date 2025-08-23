class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for idx in range(len(nums) - 2):
            left, right = idx + 1, len(nums) - 1
            while(left < right):
                check_sum = nums[idx] + nums[right] + nums[left]
                if(check_sum - target == 0):
                    return check_sum
                elif(check_sum > target):
                    right -= 1
                else:
                    left += 1
                if(abs(check_sum - target) < abs(closest_sum - target)):
                    closest_sum = check_sum
        return closest_sum