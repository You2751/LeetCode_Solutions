class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        def check(nums1, nums2):
            result = 0
            counter = Counter(nums2)
            for num in nums1:
                target = num ** 2
                left, right = 0 , len(nums2) - 1
                while(left < right):
                    check_val = nums2[left] * nums2[right]
                    if(check_val > target):
                        right -= 1
                    elif(check_val < target):
                        left += 1
                    else:
                        if(nums2[left] == nums2[right]):
                            n = counter[nums2[left]]
                            result += (n * (n - 1)) // 2
                            break
                        else:
                            result += counter[nums2[left]] * counter[nums2[right]]
                            check_left = nums2[left]
                            check_right = nums2[right]
                        while(left < right and nums2[left] == check_left):
                            left += 1
                        while(left < right and nums2[right] == check_right):
                            right -= 1
            return result
        return check(nums1, nums2) + check(nums2, nums1) 