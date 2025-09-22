class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev_idx = -1
        prev_char = 'L'
        arr = list(dominoes)
        n = len(arr)

        for i in range(n + 1):
            curr_char = 'R' if i == n else dominoes[i]
            if(curr_char == '.'):
                continue
            if(prev_char == curr_char):
                for j in range(prev_idx + 1, i):
                    arr[j] = curr_char
            elif(prev_char == 'R' and curr_char == 'L'):
                left = prev_idx + 1
                right = i - 1
                while(left < right):
                    arr[left] = 'R'
                    arr[right] = 'L'
                    left += 1
                    right -= 1
            prev_idx, prev_char = i, curr_char
        
        return ''.join(arr)