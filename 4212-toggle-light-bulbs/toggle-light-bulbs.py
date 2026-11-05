class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        result = []
        counter = Counter(bulbs)
        for key, val in counter.items():
            if(val % 2 == 1):
                result.append(key)
        return sorted(result)