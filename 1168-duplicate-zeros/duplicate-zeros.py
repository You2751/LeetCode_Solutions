class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        read = n - 1
        write = n + zeros - 1
        while(read < write):
            if(write < n):
                arr[write] = arr[read]
            if(arr[read] == 0):
                write -= 1
                if(write < n):
                    arr[write] = 0
            read -= 1
            write -= 1
        
