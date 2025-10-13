class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        mod = 10**9 + 7
        result = 0
        n = len(arr)
        for i in range(n - 2):
            t = target - arr[i]
            left, right = i + 1, n - 1
            while(left < right):
                check_sum = arr[left] + arr[right]
                if(check_sum > t):
                    right -= 1
                elif(check_sum < t):
                    left += 1
                else:
                    if(arr[left] != arr[right]):
                        left_count = right_count = 1
                        while(left + 1 < right and arr[left] == arr[left + 1]):
                            left_count += 1
                            left += 1
                        while(right - 1 > left and arr[right] == arr[right - 1]):
                            right_count += 1
                            right -= 1
                        result += left_count * right_count
                        result %= mod
                        left += 1
                        right -= 1
                    else:
                        count = right - left + 1
                        result += (count * (count - 1)) // 2
                        result %= mod
                        break
        return result