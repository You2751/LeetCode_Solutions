class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        ans = 0
        
        for i in range(n):
            t = target - arr[i]
            left, right = i + 1, n - 1
            
            while left < right:
                if arr[left] + arr[right] < t:
                    left += 1
                elif arr[left] + arr[right] > t:
                    right -= 1
                else:
                    # arr[left] + arr[right] == t
                    if arr[left] != arr[right]:
                        # Count duplicates
                        l_count = 1
                        r_count = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            l_count += 1
                            left += 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            r_count += 1
                            right -= 1
                        ans += l_count * r_count
                        ans %= MOD
                        left += 1
                        right -= 1
                    else:
                        # arr[left] == arr[right], combination C(n,2)
                        count = right - left + 1
                        ans += count * (count - 1) // 2
                        ans %= MOD
                        break  # all pairs are counted
            
        return ans % MOD
