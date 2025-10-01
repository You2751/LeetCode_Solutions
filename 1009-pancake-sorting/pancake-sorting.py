class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []

        for curr_idx in range(n - 1, 0, -1):
            target_val = curr_idx + 1
            target_idx = curr_idx
            
            while(target_idx > 0 and arr[target_idx] != target_val):
                target_idx -= 1
            
            if(target_idx < curr_idx):
                if(target_idx > 0):
                    flips.append(target_idx + 1)
                    arr[:target_idx + 1] = arr[:target_idx + 1][::-1]
                flips.append(curr_idx + 1)
                arr[:curr_idx + 1] = arr[:curr_idx + 1][::-1]
        return flips