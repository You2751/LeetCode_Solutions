class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = float('inf')
        #land first
        land_end_time = float('inf')
        for idx in range(len(landStartTime)):
            total_land_time = landStartTime[idx] + landDuration[idx]
            land_end_time = min(land_end_time, total_land_time)
        
        for idx in range(len(waterStartTime)):
            if(land_end_time >= waterStartTime[idx]):
                total_time = land_end_time + waterDuration[idx]
            else:
                total_time = waterStartTime[idx] + waterDuration[idx]
            result = min(result, total_time)
        #water first
        water_end_time = float('inf')
        for idx in range(len(waterStartTime)):
            water_end_time = min(water_end_time, waterStartTime[idx] + waterDuration[idx])

        for idx in range(len(landStartTime)):
            if(water_end_time >= landStartTime[idx]):
                total_time = water_end_time + landDuration[idx]
            else:
                total_time = landStartTime[idx] + landDuration[idx]
            result = min(result, total_time)
        
        return result