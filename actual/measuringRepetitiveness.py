from matplotlib import pyplot as pyp


def calcRelativeEntropy(seq, resCodes):
    """
    Calculate a relative entropy value for the residues in a
    sequence compared to a uniform null hypothesis
    :param seq:
    :param resCodes:
    :return:
    """
    from math import log
    N = float(len(seq))
    base = 1.0 / len(resCodes)
    prop = {}

    for r in resCodes:
        prop[r] = 0
    for r in seq:
        prop[r] += 1

    for r in resCodes:
        prop[r] /= N

    H = 0
    for r in resCodes:
        if prop[r] != 0.0:
            h = prop[r] * log(prop[r] / base, 2.0)
            H += h

    H /= log(base, 2.0)

    return H


def relativeEntropySearch(seq, winSize, isProtein=False):
    """
    Scan a sequence for repetitiveness by calculating relative
    information entropy
    :param seq:
    :param winSize:
    :param isProtein:
    :return:
    """
    lenSeq = len(seq)
    scores = [0.0] * lenSeq

    extraSeq = seq[:winSize]
    seq += extraSeq

    if isProtein:
        resCodes = "ACDEFGHIKLMNPQRSTVWY"
    else:
        resCodes = "GCAT"

    for i in range(lenSeq):
        subSeq = seq[i: i + winSize]
        scores[i] = calcRelativeEntropy(subSeq, resCodes)

    return scores


seq = "AGCTCGCTCGCTGCGTATAAAATCGCATCGCGCGCAGC"

scores = relativeEntropySearch(seq, 10)

print(scores)
pyp.title("Measuring Repetitiveness")
pyp.plot(scores)
pyp.show()
