class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        number = 0
        left, right = 0, len(nums) - 1
        while(left <= right):
            if(left != right):
                str_num = str(nums[left]) + str(nums[right])
                print(str_num)
                number += int(str_num)
            else:
                str_num = str(nums[left])
                number += int(str_num)
            print(number)
            left += 1
            right -= 1
        return number
7