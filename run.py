import requests
import csv
import os
import re
import sys

def download_file(url, filename):
  r = requests.get(url, stream=True)
  with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk: # filter out keep-alive new chunks
        f.write(chunk)
  return filename

def transform_mapping_name(name):
  return re.sub(r".sparql", '.ttl', re.sub(r'^mapping', 'target', name))

try:
    os.stat('target')
except:
    os.mkdir('target')

counter = 0
# Parsing mapping file
with open('mapping.csv', 'r') as mapping_file:
  mapping_dict = csv.DictReader(mapping_file)
  for line in mapping_dict:
    print 'Magic happening on line ' + str(counter) + " ", line, "..."

    if line['format'] == 'csv':
      download_file(line['url'], 'tmp_file')
      os.system('./tarql-1.1/bin/tarql --delimiter=comma ' + line['mapping'] + ' tmp_file >> target/' + transform_mapping_name(line['mapping']))
      os.remove('tmp_file')

    elif line['format'] == 'dsv':
      download_file(line['url'], 'tmp_file')
      os.system('./tarql-1.1/bin/tarql --delimiter=dash ' + line['mapping'] + ' tmp_file >> target/' + transform_mapping_name(['mapping']))
      os.remove('tmp_file')

    elif line['format'] == 'scsv':
      download_file(line['url'], 'tmp_file')
      os.system('./tarql-1.1/bin/tarql --delimiter=semicolon ' + line['mapping'] + ' tmp_file >> ' + transform_mapping_name(line['mapping']))
      os.remove('tmp_file')

    elif line['format'] == 'json':
      download_file(line['url'], 'tmp_file')
      os.system('java -jar jarql.jar tmp_file ' + line['mapping'] + ' >> ' + transform_mapping_name(line['mapping']))
      os.remove('tmp_file')

    else :
      print 'File format not found!!'
      sys.exit(1)

    counter += 1
    print "Done"

print "The End!"
