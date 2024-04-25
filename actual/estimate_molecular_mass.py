def estimateMolecularMass(seq, molType="protein"):
    """
    Calculate the molecular weight of a biological sequence
    assuming normal isotopic ratios and protonation/modification states
    :param seq:
    :param molType:
    :return:
    """
    residueMasses = {
        "DNA": {"G": 329.21, "C": 289.18, "A": 323.21, "T": 304.19},
        "RNA": {"G": 345.21, "C": 305.18, "A": 329.21, "U": 302.16},
        "protein": {"A": 71.07, "R": 156.18, "N": 114.08, "D": 115.08,
                    "C": 103.10, "Q": 128.13, "E": 129.11, "G": 57.05,
                    "H": 137.14, "I": 113.15, "L": 113.15, "K": 128.17,
                    "M": 131.19, "F": 147.17, "P": 97.11, "S": 87.07,
                    "T": 101.10, "W": 186.20, "Y": 163.17, "V": 99.13}
    }

    if molType not in list(residueMasses.keys()):
        raise Exception(f"{molType} is not an acceptable molType. Use one of these: protein, DNA or RNA.")
    massDict = residueMasses[molType]

    molMass = 18.02

    for letter in seq:
        molMass += massDict.get(letter, 0.0)

    return molMass


proteinSeq = "IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ"

proteinMass = estimateMolecularMass(proteinSeq, "protein")
print(proteinMass)

dnaSeq = "ATTGCCAAATGGCCATCC"
dnaMass = estimateMolecularMass(dnaSeq, "DNA")
print(dnaMass)

