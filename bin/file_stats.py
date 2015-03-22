#!/usr/bin/env python

import sys

def file_stats(input_file):
  lc = wc = cc = 0
  for line in input_file:
    lc += 1
    wc += len(line.split())
    cc += len(line)
  return (lc, wc, cc)

if len(sys.argv) != 2:
  exit("Usage: file_stats.py <filename>")

filename = sys.argv[1]
try:
  input_file = open(filename)
except IOError as e:
  print >>sys.stderr, "Couldn't open {}: {}".format(filename, e.strerror)
  sys.exit(1)
else:
  (lc, wc, cc) = file_stats(input_file)
  print "\t{} {} {} {}".format(lc, wc, cc, filename)
