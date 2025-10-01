class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flip_sequence = []
        def reverse(array, right):
            left = 0
            while(left < right):
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        for curr_position in range(n - 1, 0 , -1):
            target_value = curr_position + 1
            target_idx = curr_position
            while(target_idx > 0 and arr[target_idx] != target_value):
                target_idx -= 1
            if(target_idx < curr_position):
                if(target_idx > 0):
                    flip_sequence.append(target_idx + 1)
                    reverse(arr, target_idx)
                flip_sequence.append(curr_position + 1)
                reverse(arr, curr_position)
        
        return flip_sequence