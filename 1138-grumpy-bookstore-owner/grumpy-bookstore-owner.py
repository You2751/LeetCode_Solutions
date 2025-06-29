class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window = minutes
        total_satisfied = max_extra = extra_satisfied = 0
        for right, customer in enumerate(customers):
            if(not grumpy[right]):
                total_satisfied += customer
            else:
                extra_satisfied += customer
            if(right >= window and grumpy[right - window] == 1):
                extra_satisfied -= customers[right - window]
            max_extra = max(max_extra, extra_satisfied)
        return total_satisfied + max_extra