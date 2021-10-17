"""
CP1404 Practical 8
Car class test code
Henry Vooren
"""

from Prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Car", 140)
    my_taxi.drive(40)
    print("trip fuel =", my_taxi.fuel)
    print("trip odo =", my_taxi.odometer)
    print("trip fare =", my_taxi.get_fare())
    print(my_taxi)

    my_taxi.start_fare()
    my_taxi.drive(100)
    print("trip fuel =", my_taxi.fuel)
    print("trip odo =", my_taxi.odometer)
    print("trip fare =", my_taxi.get_fare())
    print(my_taxi)


main()
