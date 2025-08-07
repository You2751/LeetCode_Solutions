class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        idx = profit = best = 0
        for ability in worker:
            while(idx < len(jobs) and ability >= jobs[idx][0]):
                best = max(best, jobs[idx][1])
                idx += 1
            profit += best
        return profit