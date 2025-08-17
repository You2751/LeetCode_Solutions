class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            stack = []
            for right in range(len(string)):
                if(stack and string[right] == '#'):
                    stack.pop()
                elif(string[right] != '#'):
                    stack.append(string[right])
            print(stack)
            return "".join(stack)
        return helper(s) == helper(t)