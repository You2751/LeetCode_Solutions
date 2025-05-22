class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = defaultdict(int)
        for response in responses:
            response = list(set(response))
            for word in response:
                counter[word] += 1
        counter = sorted(counter.items(), key = lambda x:(-x[1], x[0]))
        print(counter)
        return counter[0][0]
