class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_unsatsified_cust = sum(cust * grum for cust, grum in zip(customers, grumpy))
        temp_cust = 0
        for i in range(minutes):
            temp_cust += customers[i] * grumpy[i]
        total_cust = temp_cust
        for i in range(minutes, len(customers)):
            temp_cust += customers[i] * grumpy[i]
            temp_cust -= customers[i - minutes] * grumpy[i - minutes]
            total_cust = max(total_cust, temp_cust)
        for i in range(len(customers)):
            if(not grumpy[i]):
                total_cust += customers[i]
        return total_cust