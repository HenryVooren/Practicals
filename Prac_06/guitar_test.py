"""
CP1404/CP5632 Practical
Test code for the guitar class methods
"""

from Prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
ibanez = Guitar("Ibanez MGM-8", 2015, 1765.00)
grover_jackson = Guitar("Grover-Jackson DK2", 1971, 9180.00)


"""using the example formatting... expecting/got..."""
print(f"Gibson L-5 CES get_age(), expected 99, got {gibson.get_age()}.")
print(f"Ibanez MGM-8 get_age(), expected 6, got {ibanez.get_age()}.")
print(f"Gibson L-5 CES is_vintage, expected True, got {gibson.is_vintage()}.")
print(f"Ibanez MGM-8, is_vintage, expected False, got {ibanez.is_vintage()}.")

print(f"Grover-Jackson DK2 is_vintage(), expected True, got {grover_jackson.is_vintage()}.")

print(gibson)
print(ibanez)
print(grover_jackson)
