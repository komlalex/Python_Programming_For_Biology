import os.path
from urllib.request import urlretrieve
from Bio import SeqIO
from os import listdir

genomeUrl = ("https://raw.githubusercontent.com/zaneveld/full_spectrum_bioinformatics/master/content"
             "/06_biological_sequences/Human_FMR1_Protein_UniProt.fasta")

genomeFileName = "HumanFMR1_Protein_Uniprot.fasta"

urlretrieve(genomeUrl, genomeFileName)

# listdir()
if os.path.exists("./HumanFMR1_Protein_Uniprot.fasta"):
    fileObj = open("HumanFMR1_Protein_Uniprot.fasta", "r")
    for protein in SeqIO.parse(fileObj, "fasta"):
        print(protein.id)
        print(protein.seq)


fh = open("HumanFMR1_Protein_Uniprot.fasta", "r")
for line in fh:
    print(line)