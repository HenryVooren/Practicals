"""
CP1404/CP5632
Language client program to use the programming languages class
"""

from Prac_06.programming_language import ProgrammingLanguage


def check_class_array(array):
    """simple check for is_dynamic method"""
    for language in array:
        if language.is_dynamic():
            print(language.name)


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    c_sharp = ProgrammingLanguage("C#", "Static", True, 2000)
    print(c_sharp)

    language_list = [ruby, python, visual_basic, c_sharp]
    print("The dynamically type languages are:")
    check_class_array(language_list)


main()
