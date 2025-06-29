class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window = minutes
        total_customers = max_customers = extra_customers = 0
        for idx, customer in enumerate(customers):
            if(not grumpy[idx]):
                total_customers += customer
            else:
                extra_customers += customer
            if(idx >= window and grumpy[idx - window] == 1):
                extra_customers -= customers[idx - window]
            max_customers = max(max_customers, extra_customers)
        return total_customers + max_customers