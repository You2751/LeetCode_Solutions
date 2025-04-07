class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        n = len(arr)
        for i in range(n - 1):
            if(arr[i] < arr[i + 1]):
                break
        else:
            return num
        max_idx, max_val = i + 1, arr[i + 1]
        for j in range(i + 1, n):
            if(arr[j] >= max_val):
                max_idx = j
                max_val = arr[j]
        left_idx = i
        for j in range(i, -1, -1):
            if(arr[j] < max_val):
                left_idx = j
        arr[left_idx], arr[max_idx] = arr[max_idx], arr[left_idx]
        return int(''.join(arr))