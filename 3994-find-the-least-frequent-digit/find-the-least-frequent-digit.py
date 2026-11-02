class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dic = defaultdict(int)
        for c in str(n):
            dic[c] += 1
        dic = sorted(dic.items(), key = lambda x:(x[1], x[0]))
        print(dic)
        return int(dic[0][0])