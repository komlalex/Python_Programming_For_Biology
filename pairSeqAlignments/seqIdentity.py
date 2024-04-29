def calcSeqIdentity(seqA, seqB):
    numPlaces = min(len(seqA), len(seqA))

    score = 0

    for i in range(numPlaces):
        if seqA[i] == seqB[i]:
            score += 1.0

    return score / numPlaces * 100.0

seq1 = "ALIGNMENTS"
seq2 = "ALIGDVENTS"
seq3 = "ALIGDPVENTS"
seq4 = "ALIGN-MENTS"

print(calcSeqIdentity(seq1, seq2))
print(calcSeqIdentity(seq1, seq3))
print(calcSeqIdentity(seq4, seq3))
