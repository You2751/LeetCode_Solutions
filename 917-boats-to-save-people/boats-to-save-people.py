class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort()
        left, right = 0, len(people) - 1
        while(left <= right):
            check = people[left] + people[right]
            if(check <= limit):
                left += 1
            result += 1
            right -= 1
        return result