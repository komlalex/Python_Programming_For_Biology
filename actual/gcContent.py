from matplotlib import pyplot

seq = "AGCTCGCTCGCTGCGTATAAAATCGCATCGCGCGCAGCTTTCCCCCCCCCCCCCCCCCCCCCCC"


def calcGcContent(seq, winSize=10):
    """
    For every window size (winSize) sub-sequences, the gc content is found. All the results
    are then returned in the form of a list.
    :param seq:
    :param winSize:
    :return:
    """
    gcValues = []

    for i in range(len(seq) - winSize):
        subSeq = seq[i:i + winSize]
        numGc = subSeq.count("G") + subSeq.count("C")
        value = numGc / float(winSize)
        gcValues.append(value)

    return gcValues


gcResult = calcGcContent(seq, 20)

pyplot.title("GC Content of DNA Sequence")
pyplot.xlabel("Sub-sequence")
pyplot.ylabel("GC Content")
pyplot.plot(gcResult)
pyplot.show()
