"""
CP1404 Practical 8
unreliable car class test code
Henry Vooren
"""

from Prac_08.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Car", 140, 0.3)  # reliability from 0 to 1
    my_car.drive(40)
    print("trip 1 fuel =", my_car.fuel)
    print("trip 1 odo =", my_car.odometer)
    print(my_car)

    my_car.drive(100)
    print("trip 2 fuel =", my_car.fuel)
    print("trip 2 odo =", my_car.odometer)
    print(my_car)


main()
