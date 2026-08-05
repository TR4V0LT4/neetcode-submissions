class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = {}

        for i,car in enumerate(position):
            cars[car] = speed[i]

        for car in sorted(cars.keys(),reverse=True):
            # print(car)
            # print(cars[car])
            # index = position.index(car)
            # car_speed = speed[index]
            time = (target - car) / cars[car]
            if not stack or time > stack[-1]:
                    stack.append(time)
            

        return len(stack)