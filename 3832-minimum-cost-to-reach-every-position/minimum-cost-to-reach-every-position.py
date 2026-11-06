class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        min_cost = cost[0]
        for i in range(1, len(cost)):
            min_cost = min(min_cost, cost[i])
            cost[i] = min_cost
        return cost