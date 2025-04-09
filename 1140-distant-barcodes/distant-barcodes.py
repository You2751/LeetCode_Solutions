class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        result = [False] * len(barcodes)
        counter = sorted(counter.items(), key = lambda x:x[1], reverse = True)
        idx = 0
        for key, val in counter:
            while(val > 0):
                if(idx >= len(result)):
                    idx = 1
                result[idx] = key
                val -= 1
                idx += 2
        return result