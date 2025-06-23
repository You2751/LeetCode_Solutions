class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_basket = defaultdict(int)
        running_fruits = max_fruits = left = 0
        for right, fruit in enumerate(fruits):
            fruits_basket[fruit] += 1
            running_fruits += 1
            if(len(fruits_basket) > 2):
                fruits_basket[fruits[left]] -= 1
                if(fruits_basket[fruits[left]] == 0):
                    del fruits_basket[fruits[left]]
                left += 1
                running_fruits -= 1
            max_fruits = max(max_fruits, running_fruits)
        return max_fruits