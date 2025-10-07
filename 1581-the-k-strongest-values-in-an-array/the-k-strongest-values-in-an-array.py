class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr) 
        mid = arr[(n - 1) // 2]
        result = []
        left, right = 0, n - 1
        for _ in range(k):
            if(abs(arr[right] - mid) > abs(arr[left] - mid)):
                result.append(arr[right])
                right -= 1
            elif(abs(arr[right] - mid) == abs(arr[left] - mid) and arr[right] > arr[left]):
                result.append(arr[right])
                right -= 1
            else:
                result.append(arr[left])
                left += 1
        return result