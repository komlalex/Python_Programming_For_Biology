class Molecule:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return f"This molecule is {self.name}"

    def getCapitalisedName(self):
        name = self.name
        if name:
            return name.capitalize()
        else:
            return name


col = Molecule(None)
print(col.getName())
print(col.getCapitalisedName())


