"""
CP1404 Practical 8
Silver taxi class
Henry Vooren
"""
from Prac_08.taxi import Taxi


class SilverTaxi(Taxi):

    def __init__(self, name, fuel, fanciness_rating):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness_rating = fanciness_rating
        self.flagfall = 4.50

    def __str__(self):
        """flagfall added to the string method"""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip with flagfall adjustment"""
        return super().get_fare()*self.fanciness_rating+self.flagfall
