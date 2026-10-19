class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        start_idx = min(start, destination)
        end_idx = max(start, destination)
        check = sum(distance[start_idx:end_idx])
        result = min(check, total - check)
        return result