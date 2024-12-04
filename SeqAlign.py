from Bio import AlignIO, SeqIO
from Bio.Align.Applications import MafftCommandline
import subprocess


sequences = [s for s in SeqIO.parse('project_sequences/human.fa', 'fasta')]

alignment = AlignIO.read('project_sequences/human.fa', 'fasta')
print(alignment)

max_len = max([len(s.seq) for s in sequences])
GAPs = "-"
for seq in sequences:
    padding = GAPs*(max_len - len(seq.seq)) # creating the padding string
    seq.seq += padding

SeqIO.write(sequences, 'paddedseq.fa', 'fasta')


mafft_exe = "mafft"
in_file = "project_sequences/human.fa"
mafft_cline = MafftCommandline(mafft_exe, input=in_file)
print(mafft_cline)

with open("./alignedSeq.fasta", "w") as outfile:
    subprocess.run(str(mafft_cline), shell=True, stdout=outfile)