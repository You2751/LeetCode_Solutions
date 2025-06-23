class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result, check = set(), set()
        for i in range(len(s) - 9):
            string = s[i:i + 10]
            if(string in check):
                result.add(string)
            check.add(string)
        return list(result)