def estimateCharge(seq, pH):
    pKaDict = {'+': 8.0, '-': 3.1, 'K': 10.0, 'R': 12.0,
               'H': 6.5, 'E': 4.4, 'D': 4.4, 'Y': 10.0, 'C': 8.5}
    isAcid = {'+': False, '-': True, 'K': False, 'R': False,
              'H': False, 'E': True, 'D': True, 'Y': True, 'C': True}

    total = 0
    for aminoAcid in seq:
        pKa = pKaDict.get(aminoAcid)

        if pKa is not None:
            r = 10 ** (pH - pKa)
            dissociated = r / (r + 1.0)

            if isAcid[aminoAcid]:
                charge = -1.0 * dissociated
            else:
                charge = 1.0 - dissociated
            total += charge

    return total


def estimateIsoelectric(sequence):
    sequence = "-" + sequence + "+"
    bestValue = 0.0
    increment = 7.0
    minCharge = estimateCharge(sequence, bestValue)

    while abs(minCharge) > 0.001:
        pHtest = bestValue + increment
        charge = estimateCharge(sequence, pHtest)

        if abs(charge) < abs(minCharge):
            minCharge = charge
            bestValue = pHtest
        else:
            increment = abs(increment) / 2.0
            if minCharge < 0.0:
                increment *= -1
    return bestValue


sequence = "HEYDHEYHEYYYDDDYRCRRCCCR"

pI = estimateIsoelectric(sequence)
print(pI)
