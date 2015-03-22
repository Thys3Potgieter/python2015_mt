def gc_content(dna_str):
  bases = 'GATC'
  counts = dict()
  total = 0
  for base in bases:
    counts[base] = dna_str.upper().count(base)
    total += counts[base]
  gc_perc = float(counts['G'] + counts['C']) / total * 100
  return gc_perc
