class Dog:
    def __init__(self, name=''):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __str__(self):
        return "{} knows how to do {}".format(self.name, self.tricks)