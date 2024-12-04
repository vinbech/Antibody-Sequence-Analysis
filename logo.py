import logomaker as logomaker
from Bio import AlignIO
import matplotlib.pyplot as plt

alignment = AlignIO.read(open("alignedSeq.fasta"), "fasta")

alignment_sequences = []
for record in alignment:
    alignment_sequences.append(str(record.seq))



count_matrix = logomaker.alignment_to_matrix(alignment_sequences)

logomaker.Logo(count_matrix)

plt.show()