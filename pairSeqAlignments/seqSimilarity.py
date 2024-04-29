import blosum
import blosum as bl

BLOSUM62 = blosum.BLOSUM(62)

DNA2 = {
    'G': {'G': 1, 'C': -3, 'A': -3, 'T': -3, 'N': 0},
    'C': {'G': -3, 'C': 1, 'A': -3, 'T': -3, 'N': 0},
    'A': {'G': -3, 'C': -3, 'A': 1, 'T': -3, 'N': 0},
    'T': {'G': -3, 'C': -3, 'A': -3, 'T': 1, 'N': 0},
    'N': {'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N': 0}
}


def calSeqSimilarity(seqA, seqB, simMatrix):
    """
    Calculates the similarity of seqA and seqB based on a provided substitution matrix, simMatrix.
    :param seqA:
    :param seqB:
    :param simMatrix:
    :return:
    """
    numPlaces = min(len(seqA), len(seqB))
    totalScore = 0.0
    for i in range(numPlaces):
        resA = seqA[i]
        resB = seqB[i]

        totalScore += simMatrix[resA][resB]

    return totalScore


print(calSeqSimilarity(seqA="AGCATCGCTCT", seqB="AGCATCGTTTT", simMatrix=DNA2))
print(calSeqSimilarity(seqA="ALIGNMENT", seqB="AIPNVENT", simMatrix=BLOSUM62))


def pairAlignScore(alignA, alignB, simMatrix, insert=8, extended=4):
    totalScore = 0.0

    n = min(len(alignA), len(alignB))

    for i in range(n):
        resA = alignA[i]
        resB = alignB[i]

        if "-" not in (resA, resB):
            simScore = simMatrix[resA][resB]
        elif (i > 0) and ("-" in (alignA[i - 1], alignB[i - 1])):
            simScore = -extended
        else:
            simScore = - insert

        totalScore += simScore

    return totalScore


print(pairAlignScore("ALIGDPPVENTS", "ALIGN--MENTS", BLOSUM62))
print(pairAlignScore("ALIGDPPVENTS", "--ALIGNMENTS", BLOSUM62))
