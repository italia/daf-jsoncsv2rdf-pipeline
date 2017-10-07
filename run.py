import request
import csv

with open('mapping.csv', 'r') as mapping_file:
  mapping_dict = csv.DictReader(mapping_file)
  for line in files:
    print line
