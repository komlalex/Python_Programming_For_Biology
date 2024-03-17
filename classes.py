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


## SUBCLASSES

class Protein(Molecule):
    def __init__(self, name, sequence):
        super().__init__(name)
        self.sequence = sequence

    def getSequence(self):
        return self.sequence


insulin = Protein("insulin", "ADFNJHFDSG")

print(insulin.getName())
print(insulin.getCapitalisedName())
print(insulin.getSequence())
