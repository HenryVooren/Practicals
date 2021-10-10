"""
CP1404 Practical 8
unreliable car class
Henry Vooren
"""

import random

from Prac_06.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_threshold = random.randint(0, 100)/100
        if reliability_threshold < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
