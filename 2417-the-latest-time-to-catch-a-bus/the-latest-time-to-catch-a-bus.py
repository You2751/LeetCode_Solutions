class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        idx = latest_time = 0
        buses.sort()
        passengers.sort()
        for i, bus in enumerate(buses):
            count = 0
            while(idx < len(passengers) and count < capacity and passengers[idx] <= bus):
                count += 1
                idx += 1
            if(i == len(buses) - 1):
                latest_time = count

        if(latest_time < capacity):
            time = buses[-1]
        else:
            time = passengers[idx - 1] - 1
        passengers_set = set(passengers)
        while(time in passengers_set):
            time -= 1
        return time