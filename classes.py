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


class AminoAcid:
    massDict = {"A": 71.07, "R": 156}
    acceptableCodes = set(massDict.keys())


lysine = AminoAcid()
massDict = lysine.massDict
print(massDict)
print(AminoAcid.massDict)
print(lysine.acceptableCodes)
print(AminoAcid.acceptableCodes)


class AminoAcid:
    def __init__(self):
        self.code = None

    def setCode(self, code):
        self.code = code


glycine = AminoAcid()
glycine.setCode("G")

print(glycine.code)


# EXAMPLE
class Molecule:
    '''This class describes a biological molecule.'''

    def __init__(self, name):
        if not name:
            raise Exception("Name must be set to something.")
        self.name = name

    def getName(self):
        return self.name

    def getCapitalisedName(self):
        name = self.getName()
        return name.capitalize()


class Protein(Molecule):
    def __init__(self, name, sequence):
        super().__init__(name)
        self.sequence = sequence
        self.aminoAcids = []

        for code in sequence:
            aminoAcid = AminoAcid(code)
            self.aminoAcids.append(aminoAcid)

    def getAminoAcids(self):
        return self.aminoAcids

    def getSequence(self):
        return [aminoAcid.code for aminoAcid in self.aminoAcids]

    def getMass(self):
        mass = 18.02
        aminoAcids = self.getAminoAcids()
        for aminoAcid in aminoAcids:
            mass += aminoAcid.getMass()
        return mass


class AminoAcid:
    massDict = {"A": 71.05, "R": 156.18, "N": 114.08,
                "D": 103.10, "C": 103.10, "Q": 128.13,
                "E": 129.11, "G": 57.05, "H": 137.14,
                "I": 113.15, "L": 113.15, "K": 128.17,
                "M": 131.19, "F": 147.17, "P": 97.11,
                "S": 87.07, "T": 101.10, "W": 186.20,
                "Y": 163.17, "V": 99.13}
    acceptableCodes = set(massDict.keys())

    def __init__(self, code):
        if code not in self.acceptableCodes:
            text = f"code = {code}, must be in list: {sorted(self.acceptableCodes)}"
            raise Exception(text)
        self.code = code

    def getMass(self):
        return self.massDict[self.code]


water = Molecule("Aqua")
print(f"Attributes: name={water.name}")
print(water.getName())

myProtein = Protein("Fictitious", "MPKAILV")
print(myProtein.name)
print(myProtein.getSequence())
print(myProtein.getMass())

print(water.__dict__)
print(Protein.__dict__)
print(getattr(water, "name"))
print(hasattr(water, "color"))
print(water.__class__)
print(water.__doc__)
print(isinstance(water, Molecule))
print(issubclass(Protein, Molecule))
print(issubclass(Molecule, Protein))


