
class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", reflection=False, year=0000):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        else:
            return True




