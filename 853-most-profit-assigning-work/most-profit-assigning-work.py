class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        idx = result = best = 0
        for ability in worker:
            while(idx < len(jobs) and ability >= jobs[idx][0]):
                best = max(best, jobs[idx][1])
                idx += 1
            result += best
        return result