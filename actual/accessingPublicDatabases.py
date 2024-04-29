from Bio import Entrez, SeqIO, ExPASy
"""
Entrez.email = "kunalexander360@gmail.com"
handle = Entrez.einfo()
rec = Entrez.read(handle)

handle2 = Entrez.esearch(db="nucleotide", term="CRT[Gene Name] AND Plasmodium falciparum[Organism]", retmax="40")
rec_list = Entrez.read(handle2)
handle2.close()
# print(rec_list.keys())
# print(rec_list["Count"])
print(rec_list["IdList"])
print(len(rec_list["IdList"]))

idList = rec_list["IdList"]
handle3 = Entrez.efetch(db="nucleotide", id=idList, rettype="gb")
recs = list(SeqIO.parse(handle3, "gb"))
handle3.close()

for rec in recs:
    print(rec.name)
    print(rec.id)
    print(rec.description)
    print(rec.seq)
    break


"""

Entrez.email = "kunalexander360@gmail.com"
handle = Entrez.efetch(db="nucleotide", rettype="fasta", id="102465470")

dnaObj = SeqIO.read(handle, "fasta")
handle.close()

print(dnaObj.id)
print(dnaObj.description)
print(dnaObj.seq)


socketObj = ExPASy.get_sprot_raw("HBB_HUMAN")
proteinObj = SeqIO.read(socketObj, "swiss")
print("This HBB!!!")
print(proteinObj.description)
print(proteinObj.seq)
socketObj.close()