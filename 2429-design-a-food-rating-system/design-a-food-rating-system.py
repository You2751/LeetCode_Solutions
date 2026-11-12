class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foods_to_rating = defaultdict(int)
        self.food_to_cuisine = defaultdict(str)
        self.heaps = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            heapq.heappush(self.heaps[cuisine], (-rating, food))
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.heaps[cuisine], (-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while(-heap[0][0] != self.foods_to_rating[heap[0][1]]):
            heapq.heappop(heap)
        return heap[0][-1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)