class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total = len(wall)
        max_prefix = 0
        prefix = defaultdict(int)
        for row in wall:
            curr_sum = 0
            for v in row[:-1]:
                curr_sum += v
                prefix[curr_sum] += 1
                max_prefix = max(max_prefix, prefix[curr_sum])
        return total - max_prefix