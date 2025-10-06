class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def compare(query):
            ptr = 0
            for c in query:
                if(ptr < len(pattern) and c == pattern[ptr]):
                    ptr += 1
                elif(c.isupper()):
                    return False
            return ptr == len(pattern)
        return [compare(query) for query in queries]