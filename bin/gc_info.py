#!/usr/bin/env python

import sys
import os.path
import seq_stats
import Bio.SeqIO

if len(sys.argv) != 2:
  exit("Usage: {} <FASTA file>".format(os.path.basename(sys.argv[0])))

filename = sys.argv[1]
for seq in Bio.SeqIO.parse(filename, 'fasta'):
  print "{} {}%".format(seq.id, int(seq_stats.gc_content(str(seq.seq))))
