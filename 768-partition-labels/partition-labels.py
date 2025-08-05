class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        dic = defaultdict(int)
        for idx, char in enumerate(s):
            dic[char] = idx

        left = right = 0

        for idx, char in enumerate(s):
            right = max(right, dic[char])
            if(idx == right):
                result.append(right - left + 1)
                left = right + 1
        return result