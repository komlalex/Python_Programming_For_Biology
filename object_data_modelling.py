from numpy import array


class Structure:
    """
    This is the top-most level of the data model, and it represents the
    specific molecule under consideration.
    """

    def __init__(self, name, conformation=0, pdbId=None):
        if not name or not isinstance(name, str):
            raise Exception("name must be set to a non-empty string")
        self.name = name
        self.conformation = conformation
        self.pdbId = pdbId
        self.chains = []  # For the children

    def delete(self):
        for chain in self.chains:
            chain.delete()

    def getChain(self, code):
        for chain in self.chains:
            if chain.code == code:
                return chain
        return None


structure = Structure("Chromosome Regulator", pdbId="1A12")


class Chain:
    allowedMolTypes = ("protein", "DNA", "RNA")

    def __init__(self, structure, code, molType="protein"):
        if not code:
            raise Exception("code must be set to a non-empty string")
        if molType not in self.allowedMolTypes:
            raise Exception(f"molType={molType} must be one of {self.allowedMolTypes}")

        # check that key code is not already used
        chain = structure.getChain(code)
        if chain:
            raise Exception(f"code={code} already used {chain}")

        self.structure = structure
        self.code = code
        self.molType = molType

        self.residues = []
        self.resDict = {}
        structure.chains.append(self)

    def getResidue(self, seqId):
        return self.resDict.get(seqId)

    def getAtoms(self):
        atoms = []
        for residue in self.residues:
            atoms.extend(residue.atoms)
        return atoms

    def delete(self):
        self.structure.chains.remove(self)


class Residue:
    def __init__(self, chain, seqId, code=None):
        if not seqId:
            raise Exception(f"seqId must be a non-empty string")
        residue = chain.getResidue(seqId)
        if residue:
            raise Exception(f"{seqId} already used as {residue}")

        self.chain = chain
        self.seqId = seqId
        self.code = code

        self.atomDict = {}
        self.atoms = []
        self.chain.residues.append(self)
        self.chain.resDict[seqId] = self

    def delete(self):
        for atom in self.atoms:
            atom.delete()
        del self.chain.resDict[self.seqId]
        self.chain.residues.remove(self)

    def getAtom(self, name):
        return self.atomDict.get(name)


class Atom:
    def __init__(self, residue, name, coords, element):
        if not name:
            raise Exception("name must be a non-empty string")
        atom = residue.getAtom(name)
        if atom:
            raise Exception(f"{name} already used as {atom}")
        if len(coords) != 3:
            raise Exception("Coordinates must contain three values")

        self.residue = residue
        self.name = name
        self.coords = array(coords)
        self.element = element

        self.residue.atoms.append(self)
        self.residue.atomDict[name] = self

    def delete(self):
        del self.residue.atomDict[self.name]
        self.residue.atoms.remove(self)
