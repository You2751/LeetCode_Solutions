class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_basket = defaultdict(int)
        left = running_fruits = result = 0
        for fruit in fruits:
            fruit_basket[fruit] += 1
            running_fruits += 1
            while(len(fruit_basket) > 2):
                fruit_basket[fruits[left]] -= 1
                running_fruits -= 1
                if(fruit_basket[fruits[left]] == 0):
                    del fruit_basket[fruits[left]]
                left += 1
            result = max(result, running_fruits)
        return result