class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        idx = last_board = 0
        buses.sort()
        passengers.sort()
        for i, bus in enumerate(buses):
            persons = 0
            while(idx < len(passengers) and persons < capacity and passengers[idx] <= bus):
                persons += 1
                idx += 1
            if(i == len(buses) - 1):
                last_board = persons
        passengers_set = set(passengers)
        if(last_board < capacity):
            time = buses[-1]
        else:
            time = passengers[idx - 1] - 1

        while(time in passengers_set):
            time -= 1
        return time