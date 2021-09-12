"""
CP1404/CP5632 Practical
Programming language class
"""


class ProgrammingLanguage:
    """Represents a programming language object"""

    def __init__(self, language_name="", typing="Static", reflection=False, year=0):
        """Initialises a programming language instance"""

        self.name = language_name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """simple check for typing being dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
