class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque([i for i, c in enumerate(senate) if c == 'R'])
        dire_queue = deque([i for i, c in enumerate(senate) if c == 'D'])
        idx = len(senate)
        while(radiant_queue and dire_queue):
            if(radiant_queue[0] < dire_queue[0]):
                radiant_queue.append(idx)
            else:
                dire_queue.append(idx)
            radiant_queue.popleft()
            dire_queue.popleft()
            idx += 1
        return 'Radiant' if radiant_queue else 'Dire'