"""
CP1404/CP5632 Practical
Guitars client program to use the guitar class
"""

from Prac_06.guitar import Guitar


def get_guitars():
    """Builds all guitar objects until user enters empty string"""
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

        guitar_name = input("Name: ")

    return guitars


def display_guitars(guitars):
    """loop using enumerate rather than for loop"""
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"

        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def main():
    """very simple main function"""
    print("My Guitars!")
    guitars = get_guitars()
    display_guitars(guitars)


main()
