class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        possible_vals = []
        for idx, val in enumerate(capacity):
            if(val >= itemSize):
                possible_vals.append([val, idx])
        possible_vals = sorted(possible_vals, key = lambda x:(x[0], x[1]))
        if not possible_vals:
            return -1
        return possible_vals[0][-1]