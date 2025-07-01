class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = max_extra = extra = 0
        for right in range(len(customers)):
            if(not grumpy[right]):
                satisfied += customers[right]
            else:
                extra += customers[right]
            if(right >= minutes):
                if(grumpy[right - minutes]):
                    extra -= customers[right - minutes]
            max_extra = max(max_extra, extra)
        return satisfied + max_extra