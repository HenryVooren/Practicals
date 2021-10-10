"""
CP1404 Practical 8
taxi simulator program using both taxi and silver taxi classes inheritance from car class
Henry Vooren
"""

from Prac_08.silver_service_taxi import SilverTaxi
from Prac_08.taxi import Taxi

LIST_OPTIONS = ("Q", "C", "D")
TAXI_OPTIONS = (Taxi("Prius", 100), SilverTaxi("Limo", 100, 2), SilverTaxi("Hummer", 200, 4))


def get_user_input():
    print("Q)uit, C)hoose Taxi, D)rive")
    user_input = input(">>> ").upper()
    while not(user_input in LIST_OPTIONS):
        print("Invalid option selected")
        print("Q)uit, C)hoose Taxi, D)rive")
        user_input = input(">>> ").upper()

    return user_input


def main():
    bill_to_date = 0
    current_taxi = None
    print("Let's drive!")
    user_input = get_user_input()
    while user_input != "Q":
        if user_input == "D":  # drive current taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                km_to_drive = float(input("Drive how far? "))
                current_taxi.drive(km_to_drive)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                bill_to_date += current_taxi.get_fare()

        elif user_input == "C":  # choose taxi for next trip
            print("Taxi's available")
            i = 0
            for taxi in TAXI_OPTIONS:
                print(i, taxi)
                i += 1

            user_taxi = int(input("Choose: "))
            if user_taxi > i-1 or user_taxi < 0:
                print("Invalid taxi choice")
            else:
                current_taxi = TAXI_OPTIONS[user_taxi]

        print("Bill to date: ${:.2f}".format(bill_to_date))
        user_input = get_user_input()

    print("Total trip costs: ${:.2f}".format(bill_to_date))
    print("Taxi's are now:")
    for taxi in TAXI_OPTIONS:
        print(taxi)


main()
