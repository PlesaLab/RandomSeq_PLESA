#!/usr/bin/env python
from seqfold import dg
from seqfold import dg_cache
from seqfold import fold
import csv
import subprocess
import matplotlib.pyplot as plt
import numpy as np


with open('random_strings.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    seqs = row

def calcSecondaryStructure(seq):
    cmd = "./hybrid-ss-min --NA=DNA -q " + str(seq)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    dg = p.stdout.read()
    ans = float(dg)
    return ans

seq_fold_DeltaG = [] # just returns minimum free energy
for sequence in seqs:
    DeltaG = dg(sequence, temp=37.0)
    seq_fold_DeltaG.append(DeltaG)

UNAFold_DeltaG = []
for sequence in seqs:
    DeltaG = calcSecondaryStructure(sequence)
    UNAFold_DeltaG.append(DeltaG)

x = np.array(seq_fold_DeltaG)
y = np.array(UNAFold_DeltaG)
print(y)

plt.scatter(x, y)
plt.ylabel("UNAFold score")
plt.xlabel("Seqfold score")
plt.show()



