class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_time = float('inf')
        for i in range(len(landStartTime)):
            land_total_time = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                if(land_total_time < waterStartTime[j]):
                    total_time =  waterStartTime[j] + waterDuration[j]
                    min_time = min(min_time, total_time)
                elif(land_total_time >= waterStartTime[j]):
                    min_time = min(min_time, land_total_time + waterDuration[j])

        for i in range(len(waterStartTime)):
            water_total_time = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                if(water_total_time < landStartTime[j]):
                    total_time =  landStartTime[j] + landDuration[j]
                    min_time = min(min_time, total_time)
                elif(water_total_time >= landStartTime[j]):
                    min_time = min(min_time, water_total_time + landDuration[j])   
        return min_time