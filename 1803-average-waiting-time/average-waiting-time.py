class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        total = 0
        n = len(customers) 
        prev_finish = 0
        for idx, (customer_in, customer_finish) in enumerate(customers):
            curr_start = max(customer_in, prev_finish)
            total += curr_start + customer_finish - customer_in
            prev_finish = curr_start + customer_finish
        return total / n