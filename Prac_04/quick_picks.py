"""
CP1404/CP5632 Practical
Quick lottery picks
update to commit to prac_05 feedback
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45


def get_pick_number():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 1:
        print("Invalid number of quick picks")
        quick_picks = int(input("How many quick picks? "))

    return quick_picks


def draw_line():
    line = []
    for i in range(6):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in line:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)

        line.append(number)

    line.sort()
    return line


def display_numbers(numbers):
    for i in range(len(numbers)):
        print(f"{numbers[i]}")


def main():
    quick_picks = get_pick_number()
    numbers = []
    for i in range(quick_picks):
        numbers.append(draw_line())

    # print(numbers)
    display_numbers(numbers)


main()
