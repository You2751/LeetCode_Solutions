class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        path = paths[0]
        print(path.split())
        for path in paths:
            path = path.split()
            for p in path[1:]:
                idx = p.find('(')
                file_name, content = p[:idx], p[idx + 1: -1]
                dic[content].append(path[0] + '/' + file_name)

        return [v for v in dic.values() if len(v) > 1]