class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        dic = defaultdict(int)
        for idx, c in enumerate(s):
            dic[c] = idx
        start = end = 0
        for i in range(len(s)):
            end = max(end, dic[s[i]])
            if(i == end):
                result.append(end - start + 1)
                start = i + 1
        return result