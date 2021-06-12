"""
 Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        return f"You're on your way"

    def stop(self):
        return f"You've stopped"

    def turn(self, direction):
        return f"You turned {direction}"

    def show_speed(self):
        return f"Your speed is {self.speed} km/h"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Attention! You have exceeded the speed limit."
        else:
            return f"Your speed is {self.speed} km/h"


class SportCar(Car):
    def on_sport(self):
        return f"You have turned on the sports mode"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Attention! You have exceeded the speed limit."
        else:
            return f"Your speed is {self.speed} km/h"


class PoliceCar(Car):
    is_police = True


# car('', '', 10)
police = PoliceCar('BMW', 'white', 60)
print(police.is_police)
print(police.show_speed())
print(police.turn('right'))
print("#############")
town_car = TownCar('trolleybus', 'red', 80)
print(town_car.is_police)
print(town_car.show_speed())
print("#############")
town_car_2 = TownCar('bus', 'yellow', 30)
print(town_car_2.show_speed())
print(town_car_2.turn('left'))
print("#############")
sport_car = SportCar('Ferrari', 'red', 250)
print(sport_car.name)
print(sport_car.on_sport())
