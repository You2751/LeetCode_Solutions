class Solution:
    def nextGreaterElement(self, n: int) -> int:
        string = list(str(n))
        idx1 = len(string) - 1
        while(idx1 > 0 and string[idx1 - 1] >= string[idx1]):
            idx1 -= 1
        if(idx1 == 0):
            return -1
        idx2 = len(string) - 1
        while(idx2 > idx1 - 1 and string[idx1 - 1] >= string[idx2]):
            idx2 -= 1
        string[idx1 - 1], string[idx2] = string[idx2], string[idx1 - 1]
        string[idx1:] = string[idx1:][::-1]
        result = int("".join(string))
        return result if result <= 2**31 - 1 else -1