"""
CP1404/CP5632 Practical
Guitar class
"""


class Guitar:
    """Represents guitar object"""

    def __init__(self, guitar_name="", year=0, cost=0):
        """initiates guitar object"""
        self.name = guitar_name
        self.year = year
        self.cost = cost

    def __str__(self):
        """example string format put year in brackets"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        current_year = 2021
        return current_year - self.year

    def is_vintage(self):
        """using self get age method"""
        if self.get_age() >= 50:
            return True
        else:
            return False

