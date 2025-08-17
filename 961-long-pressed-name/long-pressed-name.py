class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = ptr2 = 0
        while(ptr1 < len(name) and ptr2 < len(typed)):
            if(name[ptr1] == typed[ptr2]):
                ptr1 += 1
                ptr2 += 1
            elif(name[ptr1] != typed[ptr2] and ptr2 > 0 and typed[ptr2] == typed[ptr2 - 1]):
                ptr2 += 1
            else:
                return False
        while(ptr2 < len(typed)):
            if(typed[ptr2] == name[-1]):
                ptr2 += 1
            else:
                return False
        return ptr1 == len(name)