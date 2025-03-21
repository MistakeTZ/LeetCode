import math

class Solution(object):
    def repairCars(self, ranks: list, cars: int):
        car_per_rank = math.ceil(cars / len(ranks))
        min_time = 10 ** 18
        print(min_time)

        while True:
            for car in range(cars):
                times = 

        
print(Solution().repairCars(ranks = [4,2,3,1], cars = 10))
print(Solution().repairCars(ranks = [5,1,8], cars = 6))