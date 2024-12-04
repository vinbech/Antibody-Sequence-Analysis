from Bio import SeqIO
from Bio import Align

human = [s for s in SeqIO.parse('project_sequences/human.fa', 'fasta')]
mouse = [s for s in SeqIO.parse('project_sequences/mouse.fa', 'fasta')]

input = "QQGNVFSCSVMHEALHNHYTQKSLSLSPGK"
#7595

bestScore = -1
bestID = -1
genome = ""
bestAlign = None

aligner = Align.PairwiseAligner()
aligner.mode = 'global'

for sequence in human:
    alignments = aligner.align(sequence.seq, input)
    alignment = alignments[0]
    score = alignment.score
    if score > bestScore:
        bestScore = score
        bestID = sequence.id
        genome = 'Human'
        bestAlign = alignment

for sequence in mouse:
    alignments = aligner.align(sequence.seq, input)
    alignment = alignments[0]
    score = alignment.score
    if score > bestScore:
        bestScore = score
        bestID = sequence.id
        genome = 'Mouse'
        bestAlign = alignment

print(f'ID: {bestID}')
print(f'Score: {bestScore}')
print(f'Genome: {genome}')
print(bestAlign)