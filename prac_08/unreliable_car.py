"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = 0
        random_number = randint(0, 100)
        # Allow the vehicle to drive if the random number generated is less than the cars reliability score
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        # Else distance driven = 0 is returned
        return distance_driven
