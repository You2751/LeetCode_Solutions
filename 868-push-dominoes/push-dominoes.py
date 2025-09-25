class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = list(dominoes)
        n = len(arr)
        prev_idx = -1
        prev_char = 'L'
        for i in range(n + 1):
            if(i == n):
                curr_char = 'R'
            else:
                curr_char = arr[i]
            if(curr_char == '.'):
                continue
            if(curr_char == prev_char):
                for j in range(prev_idx + 1, i):
                    arr[j] = prev_char
            elif(prev_char == 'R' and curr_char == 'L'):
                left = prev_idx + 1
                right = i - 1
                while(left < right):
                    arr[left] = "R"
                    arr[right] = "L"
                    left += 1
                    right -= 1
            prev_idx, prev_char = i, curr_char
        return "".join(arr)