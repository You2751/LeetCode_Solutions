class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        firstList.sort()
        secondList.sort()
        ptr1 = ptr2 = 0
        while(ptr1 < len(firstList) and ptr2 < len(secondList)):
            first_start, first_end = firstList[ptr1]
            second_start, second_end = secondList[ptr2]
            start = max(first_start, second_start)
            end = min(first_end, second_end)
            if(start <= end):
                result.append([start, end])
            if(first_end < second_end):
                ptr1 += 1
            else:
                ptr2 += 1
        return result