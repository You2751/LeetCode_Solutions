class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        pairs = 0
        dic = defaultdict(int)
        for num in time:
            remainder = 60 - (num % 60 )
            if(num % 60 == 0):
                pairs += dic[0]
            if(remainder in dic):
                pairs += dic[remainder]
            dic[num % 60] += 1
        print(dic)
        return pairs