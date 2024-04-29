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

print("\n \n \n *********************************")
fileObj3 = open("collagen2.fasta", "r")

for gene in SeqIO.parse(fileObj3, "fasta"):
    print(gene.id)
    print(gene.seq)
    print(f"Length: {len(gene.seq)}")

fj = open("output.fasta", "r")

for protein in SeqIO.parse(fj, "fasta"):
    print(protein.id)
    print(protein.seq)


fileObj = open("gene.fna", "r")

for gene in SeqIO.parse(fileObj, "fasta"):
    print(gene.id)
    print(gene.name)
    print(gene.description)
    print(gene.seq)
    print("\n")



