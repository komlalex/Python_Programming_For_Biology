from Bio import SeqIO
from Bio.SeqRecord import  SeqRecord
from Bio.Seq import Seq

proteinSeq1 = "KKKKEEEHHHH"
proteinSeq2 = "QQQQQRRRRHK"
fileObj4 = open("output.fasta", "w")

seq1 = Seq(proteinSeq1)
seq2 = Seq(proteinSeq2)

record1 = SeqRecord(seq1, id="ALEX_1 | Chains")
record2 = SeqRecord(seq2, id="ALEX_2 | Chains")
SeqIO.write([record1, record2], fileObj4, "fasta")