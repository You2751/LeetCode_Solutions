class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for idx, c in enumerate(s):
            if(c == '('):
                stack.append(idx)
            elif(c == ')'):
                if(not stack):
                    s[idx] = ""
                else:
                    stack.pop()
        while(stack):
            s[stack.pop()] = ""
        return "".join(s)