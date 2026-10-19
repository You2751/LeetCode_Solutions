class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        idx = 0
        n = len(arr)
        while(idx < n - 1 and arr[idx] < arr[idx + 1]):
            idx += 1
        if(idx == 0 or idx == n - 1):
            return False
        while(idx < n - 1 and arr[idx] > arr[idx + 1]):
            idx += 1
        return idx == n - 1