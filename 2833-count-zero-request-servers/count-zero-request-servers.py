class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        counter = defaultdict(int)
        result = [0] * len(queries)
        logs.sort(key = lambda x :x[1])
        window_end = window_start = active_servers = 0
        index_queries = sorted([query, idx] for idx, query in enumerate(queries))
        for query, idx in index_queries:
            while(window_end < len(logs) and logs[window_end][1] <= query):
                server_idx = logs[window_end][0]
                counter[server_idx] += 1
                if(counter[server_idx] == 1):
                    active_servers += 1
                window_end += 1
            while(window_start < window_end and logs[window_start][1] < query - x):
                server_idx = logs[window_start][0]
                counter[server_idx] -= 1
                if(counter[server_idx] == 0):
                    active_servers -= 1
                window_start += 1
            result[idx] = n - active_servers
        return result