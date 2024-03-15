# Multiple returns

def calcFunc(x, y):
    v = x * x + x * 2
    w = y * y - y * 2
    return v, w


v, w = calcFunc(4, 5)

print(v, w)


# Mutable arguments

def myFunc(parameter=[]):
    parameter.append(100)
    print(parameter)


myFunc()
myFunc()
myFunc()


def reverseComplement(sequence, isDNA=True):
    if isDNA:
        sequence = sequence.replace("U", "T")
        transTable = str.maketrans("ATGC", "TACG")
    else:
        sequence = sequence.replace("T", "U")
        transTable = str.maketrans("AUGC", "UACG")

    complement = sequence.translate(transTable)
    reverseComp = complement[::-1]

    return reverseComp


seq1 = "GATTACA"
seq2 = "AUGGUG"

print(reverseComplement(seq1))
print(reverseComplement(seq1, isDNA=False))
print(reverseComplement(seq2, False))


# Anonymous arguments

def testFunc(item, *args, **kw):
    print("Mandatory argument: ", item)
    print("Unnamed arguments: ", args)
    print("Keyword dictionary: ", kw)


testFunc("Hello", 1, 99, valueA="abc", valueB="7.0")

KILOS_PER_POUND = 0.45359237


def poundsToKilos(pounds):
    kilos = pounds * KILOS_PER_POUND
    return kilos


def kilosToPounds(kilos):
    pounds = kilos / KILOS_PER_POUND
    return pounds

# Lambda functions
cube = lambda x: x*x*x

print(cube(3))
