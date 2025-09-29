class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        workers.sort()
        result = max_profit = idx = 0
        jobs = sorted(zip(difficulty, profit))
        for worker in workers:
            while(idx < len(jobs) and worker >=  jobs[idx][0]):
                max_profit = max(max_profit, jobs[idx][1])
                idx += 1
            result += max_profit
        return result