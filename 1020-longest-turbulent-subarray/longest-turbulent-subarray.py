class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, prev = 1, ""
        left, right = 0, 1
        while(right < len(arr)):
            if(arr[right] > arr[right - 1] and prev != '>'):
                res = max(res, right - left + 1)
                right += 1
                prev = '>'
            elif(arr[right] < arr[right - 1] and prev != '<'):
                res = max(res, right - left + 1)
                right += 1
                prev = '<'
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev = ''
        return res