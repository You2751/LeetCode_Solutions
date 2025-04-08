class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        string = ""
        while(a + b > 0):
            if(len(string) >= 2 and string[-1] == 'a' and string[-2] == 'a'):
                string += 'b'
                b -= 1
            elif(len(string) >= 2 and string[-1] == 'b' and string[-2] == 'b'):
                string += 'a'
                a -= 1
            elif(a > b):
                string += 'a'
                a -= 1
            else:
                string += 'b'
                b -= 1
        return string