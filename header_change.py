import os
import subprocess
import sys
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

cwdir=sys.argv[1]

for file in os.listdir(cwdir):
     if file.endswith(".fasta"):
         name=file.split(".")[0]
         #print(name)
         with open(file) as original, open(name+".fasta",'w') as corrected:
             records=SeqIO.parse(original,'fasta')
             for record in records:
                 record.id=name+""+record.id
                 SeqIO.write(record, corrected, 'fasta')
