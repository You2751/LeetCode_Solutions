class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        n = len(arr)
        while(left + 1 < n and arr[left + 1] >= arr[left]):
            left += 1
        if(left == n - 1):
            return 0
        right = n - 1
        while(right - 1 >= 0 and arr[right] >= arr[right - 1]):
            right -= 1
        result = min(right, n - left - 1)
        ptr1, ptr2 = 0, right
        while(ptr1 <= left and ptr2 < n):
            if(arr[ptr2] >= arr[ptr1]):
                result = min(result, ptr2 - ptr1 - 1)
                ptr1 += 1
            else:
                ptr2 += 1
        return result