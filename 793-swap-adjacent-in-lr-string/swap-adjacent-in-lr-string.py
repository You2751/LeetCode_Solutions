class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        ptr1 = ptr2 = 0
        while(True):
            while(ptr1 < n and start[ptr1] == 'X'):
                ptr1 += 1
            while(ptr2 < n and end[ptr2] == 'X'):
                ptr2 += 1
            
            if(ptr1 >= n and ptr2 >= n):
                return True
            if(ptr1 >= n or ptr2 >= n or start[ptr1] != end[ptr2]):
                return False
            
            if(start[ptr1] == 'L' and end[ptr2] == 'L' and ptr1 < ptr2):
                return False

            if(start[ptr1] == 'R' and end[ptr2] == 'R' and ptr1 > ptr2):
                return False
            ptr1 += 1
            ptr2 += 1