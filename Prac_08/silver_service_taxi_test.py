"""
CP1404 Practical 8
Car class test code
Henry Vooren
"""


from Prac_08.silver_service_taxi import SilverTaxi


def main():
    my_silver_taxi = SilverTaxi("Car", 0, 2)
    my_silver_taxi.drive(40)
    print("trip fuel = ", my_silver_taxi.fuel)
    print("trip odo = ", my_silver_taxi.odometer)
    print("trip fare = ", my_silver_taxi.get_fare())
    print(my_silver_taxi)


main()
