from car import Car


class Solver:
    def __init__(self, cars: list, applications: list):
        self.cars = cars
        self.applications = sorted(applications, key=lambda i: i.volume)

    @staticmethod
    def max_car_volume(cars: list):
        return max([car.volume for car in cars]) if cars else 0

    @staticmethod
    def min_app_volume(applications: list):
        return min([app.volume for app in applications]) if applications else 0

    def curr_volume(self, arr: list) -> int:
        return sum([self.applications[i].volume for i in arr])

    def get_best_car(self, volume: int) -> Car:
        best_car = self.cars[0]
        for car in self.cars:
            if best_car.volume > car.volume >= volume:
                best_car = car
        return best_car

    def get_applications(self, arr: list) -> list:
        res = []
        for n in arr:
            res.append(self.applications[n])
        return res

    def run(self):
        complited_cars = {}
        while self.cars and self.applications and self.min_app_volume(self.applications) <= self.max_car_volume(self.cars):
            max_car_volume = self.max_car_volume(self.cars)
            apps_arr = [[i] for i in range(len(self.applications))]
            max_volume = 0
            max_arr = []
            is_end = False
            while apps_arr and not is_end:
                curr_arr = apps_arr.pop(-1)
                curr_vol = self.curr_volume(curr_arr)
                if curr_vol <= max_car_volume:
                    if curr_vol > max_volume:
                        max_volume = curr_vol
                        max_arr = curr_arr[:]
                    if max_volume == max_car_volume:
                        is_end = True
                    for i in range(curr_arr[0]):
                        apps_arr.append([i] + curr_arr[:])
            car = self.get_best_car(max_volume)
            self.cars.remove(car)
            appls = self.get_applications(max_arr)
            for app in appls:
                self.applications.remove(app)
            complited_cars[car] = appls
        return complited_cars
