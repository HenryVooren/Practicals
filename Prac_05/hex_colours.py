"""
CP1404/CP5632 Practical
Hexadecimal colour codes
"""

COLOUR_TO_HEXADECIMAL = {"coral": "#ff7f50", "cornflowerblue": "#6495ed", "darkorchid": "#9932cc",
                         "firebrick": "#b22222", "rebeccapurple": "#663399", "wheat": "#f5deb3", "thistle": "#d8bfd8",
                         "steelblue": "#4682b4", "sienna": "#a0522d", "palevioletred": "#db7093"}

print(COLOUR_TO_HEXADECIMAL)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_HEXADECIMAL:
        print(colour_name, "is", COLOUR_TO_HEXADECIMAL[colour_name])
    else:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").lower()
