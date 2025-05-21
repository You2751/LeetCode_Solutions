class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        string = s[:10]
        dic = defaultdict(int)
        dic[string] = 1
        for i in range(10, len(s)):
            string = string[1:]
            string += s[i]
            dic[string] += 1
        for key, val in dic.items():
            if(val >= 2):
                result.append(key)
        return result
