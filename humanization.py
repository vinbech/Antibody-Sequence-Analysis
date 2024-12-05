from Bio import SeqIO
from Bio import Align

genomes = ['human', 'mouse']
db = [[s for s in SeqIO.parse(f'project_sequences/{genome}.fa', 'fasta')] for genome in genomes]
input = "QQGNVFSCSVMHEALHNHYTQKSLSLSPGK"

bestScore = -1
bestID = -1
species = ""
bestAlign = None

aligner = Align.PairwiseAligner()
aligner.mode = 'global'

for i, genome in enumerate(db):
    for sequence in genome:
        alignment = aligner.align(sequence.seq, input)[0]
        if alignment.score > bestScore:
            bestScore = alignment.score
            bestID = sequence.id
            species = genomes[i]
            bestAlign = alignment

print(f'ID: {bestID}')
print(f'Score: {bestScore}')
print(f'Genome: {species}')
print(bestAlign)