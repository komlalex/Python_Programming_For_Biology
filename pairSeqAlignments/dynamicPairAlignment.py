from blosum import BLOSUM

BLOSUM62 = BLOSUM(62)


def sequenceAlignment(seqA, seqB, simMatrix, insert=8, extend=4):
    numI = len(seqA) + 1
    numJ = len(seqB) + 1
    scoreMatrix = [[0] * numJ for x in range(numI)]
    routeMatrix = [[0] * numJ for x in range(numI)]

    for i in range(1, numI):
        routeMatrix[i][0] = 1

    for j in range(1, numJ):
        routeMatrix[0][j] = 2

    for i in range(numI):
        for j in range(1, numJ):
            penalty1 = insert
            penalty2 = insert

            if routeMatrix[i - 1][j] == 1:
                penalty1 = extend
            elif routeMatrix[i][j - 2] == 2:
                penalty2 = extend

            similarity = simMatrix[seqA[i - 1]][seqB[j - 1]]
            paths = [scoreMatrix[i - 1][j - 1] + similarity,
                     scoreMatrix[i - 1][j] - penalty1,
                     scoreMatrix[i][j - 1] - penalty2]
            best = max(paths)
            route = paths.index(best)
            scoreMatrix[i][j] = best
            routeMatrix[i][j] = route
        alignA = []
        alignB = []
        i = numI - 1
        j = numJ - 1
        score = scoreMatrix[i][j]
        while i > 0 or j > 0:
            route = routeMatrix[i][j]
            if route == 0:
                alignA.append(seqA[i - 1])
                alignB.append(seqB[j - 1])
                i -= 1
                j -= 1
            elif route == 1:
                alignA.append(seqA[i - 1])
                alignB.append("-")
                i -= 1
            elif route == 2:
                alignA.append("-")
                alignB.append(seqB[j - 1])
                j -= 1

            alignA.reverse()
            alignB.reverse()
            alignA = "".join(alignA)
            alignB = "".join(alignB)

            return score, alignA, alignB


seqA = "WFSEPEIST"
seqB = "FSRPAVVIST"
score, alignA, alignB = sequenceAlignment(seqA, seqB, BLOSUM62)
print(score)
print(alignA)
print(alignB)
