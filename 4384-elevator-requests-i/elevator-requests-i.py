class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        prev = total = 0
        for req in requests:
            if(prev == req):
                continue
            else:
                total += abs(req - prev)
                prev = req
        return total 