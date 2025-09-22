class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #case 1 --> L..L --> fill left
        #case 2 --> R..R --> Fill Right
        #Case 3 --> R..L --> Fill between them till middle
        #Case 4 --> L..R --> Do nothing
        #Case 5 --> . --> Do nothing

        #Edge case 1 --> ....L, start with Left 
        #Edge Case 2 --> R...., end with Right 

        arr = list(dominoes)
        prev_idx = -1
        prev_char = 'L'
        n = len(dominoes)
        for i in range(n + 1):
            if(i == n):
                curr_char = 'R'
            else:
                curr_char = arr[i]
            if(curr_char == '.'):
                continue
            if(curr_char == prev_char):
                for j in range(prev_idx + 1, i):
                    arr[j] = curr_char
            elif(curr_char == 'L' and prev_char == 'R'):
                left = prev_idx + 1
                right = i - 1
                while(left < right):
                    arr[left] = 'R'
                    arr[right] = 'L'
                    left += 1
                    right -= 1
            prev_idx, prev_char = i, curr_char

        return ''.join(arr)
        