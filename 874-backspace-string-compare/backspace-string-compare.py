class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(string):
            skip = 0
            for c in string[::-1]:
                if(c == '#'):
                    skip += 1
                elif(skip > 0):
                    skip -= 1
                else:
                    yield c
        return all(x == y for x, y in zip_longest(check(s), check(t)))