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


structure = Structure("Chromosome Regulator", pdbId="1A12")

