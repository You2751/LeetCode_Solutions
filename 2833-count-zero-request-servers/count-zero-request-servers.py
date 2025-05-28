class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        result = [0] * len(queries)
        counter = defaultdict(int)
        active_servers = window_start = window_end = 0
        logs.sort(key = lambda x:x[1])
        indexed_queries = sorted([query_time, idx] for idx, query_time in enumerate(queries))

        for query_time, idx in indexed_queries:
            while(window_end < len(logs) and logs[window_end][1] <= query_time):
                server_idx = logs[window_end][0]
                counter[server_idx] += 1
                if(counter[server_idx] == 1):
                    active_servers += 1
                window_end += 1
            while(window_start < window_end and logs[window_start][1] < query_time - x):
                server_idx = logs[window_start][0]
                counter[server_idx] -= 1
                if(counter[server_idx] == 0):
                    active_servers -= 1
                window_start += 1
            result[idx] = n - active_servers
        return result