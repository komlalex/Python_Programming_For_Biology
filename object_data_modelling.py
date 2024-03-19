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


def getStructuresFromFile(fileName):
    fileObject = open(fileName)
    structure = None
    name = "unknown"
    pdbId = None
    conformation = 0
    structures = []

    for line in fileObject:
        record = line[0:6].strip()
        if record == "HEADER":
            pdbId = line.split()[-1]
        elif record == "TITLE":
            name = line[10:].strip()
        elif record == "MODEL":
            conformation = int(line[10:14])
        elif record == "ENDML":
            structure = None
        elif record == 'ATOM':
            serial = int(line[6:11])
            atomName = line[12:16].strip()
            resName = line[17:20].strip()
            chainCode = line[21:26].strip()
            seqId = int(line[22:26])
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            segment = line[72:76].strip()
            element = line[76:78].strip()

            if chainCode == "":
                if segment:
                    chainCode = segment
                else:
                    chainCode = "A"
            if not structure:
                structure = Structure(name, conformation, pdbId)
                structures.append(structure)
            chain = structure.getChain(chainCode)
            if not chain:
                chain = Chain(structure, chainCode)

            residue = chain.getResidue(seqId)
            if not residue:
                residue = Residue(chain, seqId, resName)

            if not element:
                element = name[0]
                coords = (x, y, z)
                atom = Atom(residue, atomName, coords, element)

        fileObject.close()
        return structures

    testStructs = getStructuresFromFile("./mydata/2kpf.pdb")

    structure = testStructs[0]
    chain = structure.getChain("A")

    for residue in chain.residues:
        print(residue.seqId, residue.code)
