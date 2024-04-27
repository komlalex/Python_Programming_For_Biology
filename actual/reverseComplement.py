def validateSeq(seq):
    """
    This function takes a DNA sequence and ensures that all the nucleotides are
    the standard nucleotides found in DNA. It either throws an error when an invalid
    nucleotide is found, or returns the sequence when everything is alright.
    :param seq:
    :return:
    """
    for nucleotide in seq:
        if nucleotide not in ["A", "T", "G", "C"]:
            raise Exception(f"Nucleotide {nucleotide} is invalid")
    return seq


def reverseDnaComplement(seq):
    """
    Returns the reverse complement of a DNA molecule
    :param seq:
    :return:
    """
    valSeq = validateSeq(seq)

    seq = list(valSeq)
    basePairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp = []
    for nucleotide in seq:
        comp.append(basePairs[nucleotide])

    reverseComp = comp[::-1]
    reverseComp = "".join(reverseComp)

    return reverseComp


dnaSeq = "AAATCTGTTCCGATATGG"
rev = reverseDnaComplement(dnaSeq)
print(rev)
