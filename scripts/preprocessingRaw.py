##
##
from Bio import SeqIO 

seq = SeqIO.parse("/home/rudlab/projects/coronaEnvAn/data/coronaEnv.raw.fasta","fasta")

seq_set = set() 

with open("/home/rudlab/projects/coronaEnvAn/data/coronaEnv.fasta", "w") as handle:
    for s in seq:
        if "partial" in s.description or "truncated" in s.description:
            continue
        if "X" in s.seq:
            continue 
        if "envelope protein" not in s.description:
            continue
        if s.seq not in seq_set:
            seq_set.add(s.seq)
            SeqIO.write(s, handle, "fasta") 

