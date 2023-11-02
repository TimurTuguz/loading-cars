import json
from car import Car
from application import Application

class File:
    def __init__(self):
        self.cars = []
        self.applications = []

    def get_cars(self) -> list:
        with open('dates/cars', 'r') as cars:
            for line in cars:
                car = json.loads(line)
                self.cars.append(Car(car['ident_code'], car['volume'], car['price'], car['fridge_type']))
        return self.cars

    def get_applications(self) -> list:
        with open('dates/applications', 'r') as apps:
            for line in apps:
                app = json.loads(line)
                self.applications.append(Application(app['ident_code'], app['volume'], app['fridge_type'], app['crashed']))
        return self.applications
