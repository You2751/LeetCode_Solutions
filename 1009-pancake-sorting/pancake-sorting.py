class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flip_sequence = []
        for curr_idx in range(n - 1, 0, -1):
            target_val = curr_idx + 1
            target_idx = curr_idx

            while(target_idx > 0 and arr[target_idx] != target_val):
                target_idx -= 1
            
            if(target_idx < curr_idx):
                if(target_idx > 0):
                    flip_sequence.append(target_idx + 1)
                    arr[:target_idx + 1] = arr[:target_idx + 1][::-1]
                flip_sequence.append(curr_idx + 1)
                arr[:curr_idx + 1] = arr[:curr_idx + 1][::-1]
        return flip_sequence