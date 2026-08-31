class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter("balloon")
        counter_num = defaultdict(int)
        for c in text:
            if(c in counter):
                counter_num[c] += 1

        result = float('inf')
        for key, val in counter.items():
            if key not in counter_num:
                print(key)
                return 0
            else:
                result = min(result, counter_num[key] // val)
        return result