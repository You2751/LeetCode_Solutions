class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        counter = Counter(answers)
        for group, count in counter.items():
            group_size = group + 1
            num_of_groups = ceil(count / group_size)
            total += num_of_groups * group_size
        return total