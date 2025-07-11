class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        left = right = active_servers = 0
        result = [-1] * len(queries)
        counter = defaultdict(int)
        logs.sort(key = lambda x:(x[1], x[0]))
        sorted_queries = sorted([query, idx] for idx, query in enumerate(queries))

        for query, idx in sorted_queries:
            while(right < len(logs) and logs[right][1] <= query):
                server_idx = logs[right][0]
                counter[server_idx] += 1
                if(counter[server_idx] == 1):
                    active_servers += 1
                right += 1
            while(left < right and logs[left][1] < query - x):
                server_idx = logs[left][0]
                counter[server_idx] -= 1
                if(counter[server_idx] == 0):
                    active_servers -= 1
                left += 1
            idle = n - active_servers 
            result[idx] = idle
        return result