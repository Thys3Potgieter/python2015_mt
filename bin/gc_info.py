#!/usr/bin/env python

import sys
import os.path
import seq_stats
import Bio.SeqIO

if len(sys.argv) != 2:
  exit("Usage: {} <FASTA file>".format(os.path.basename(sys.argv[0])))

filename = sys.argv[1]
try:
  input_file = open(filename)
except IOError as e:
  print >>sys.stderr, "Could not open {}: {}\n".format(filename, e.strerror)
  sys.exit(1)
else:
  for record in Bio.SeqIO.parse(input_file, 'fasta'):
    seq_str = str(record.seq)
    gc_perc = int(seq_stats.gc_content(seq_str))
    print "{} {}%".format(record.id, gc_perc)
