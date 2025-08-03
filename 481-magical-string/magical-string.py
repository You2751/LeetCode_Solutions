class Solution:
    def magicalString(self, n: int) -> int:
        idx = 2
        pre = [1, 2, 2]
        while(len(pre) < n):
            last_val = pre[-1]
            factor = 3 - last_val
            pre += [factor] * pre[idx]
            idx += 1
        return pre[:n].count(1)