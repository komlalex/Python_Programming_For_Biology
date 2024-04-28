from Bio import SeqIO

fileObj = open("collagen.fasta")

for protein in SeqIO.parse(fileObj, "fasta"):
    print(protein.id)
    print(protein.seq)
    print(len(protein.seq))


fileObj2 = open("m2k2.fasta", "r")

for protein in SeqIO.parse(fileObj2, "fasta"):
    print(protein.id)
    print(protein.seq)
