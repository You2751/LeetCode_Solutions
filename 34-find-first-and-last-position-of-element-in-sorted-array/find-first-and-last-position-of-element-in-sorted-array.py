class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect(find_first):
            result = -1
            left, right = 0, len(nums) - 1
            while(left <= right):
                mid = (left + right) // 2
                if(nums[mid] == target):
                    result = mid
                    if(find_first):
                        right = mid - 1
                    else:
                        left = mid + 1
                elif(nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1
            return result
        first_idx = bisect(True)
        last_idx = bisect(False)
        return [first_idx, last_idx]