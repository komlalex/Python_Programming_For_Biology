seq = "AAAGGGTCGCCATTA"


def revComplement(sequence, isDNA=True):
    if isDNA:
        sequence = sequence.replace("U", "T")
        maketrans = str.maketrans("ATGC", "TACG")
        complement = sequence.translate(maketrans)
    else:
        sequence = sequence.replace("T", "U")
        maketrans = str.maketrans("AUGC", "UACG")
        complement = sequence.translate(maketrans)

    reverseComp = complement[::-1]
    return reverseComp


result = revComplement(seq)

print(result)
