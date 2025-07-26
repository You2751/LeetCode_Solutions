class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(string):
            stack = []
            for c in string:
                if(stack and c == '#'):
                    stack.pop()
                elif(c != '#'):
                    stack.append(c)
            return "".join(stack)
        return check(s) == check(t)