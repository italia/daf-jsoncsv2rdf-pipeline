import requests
import csv
import tarfile
import os
import re

def download_file(url, filename):
  r = requests.get(url, stream=True)
  with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk: # filter out keep-alive new chunks
        f.write(chunk)
  return filename

def transform_mapping_name(name):
  return re.sub(r".sparql", '.ttl', re.sub(r'^mapping', 'target', name))


# Download jarql
print "Downloading Jarql..."
download_file('https://github.com/linked-solutions/jarql/releases/download/jarql-1.0.0/jarql-1.0.0.jar', 'jarql.jar')
print "Done"

# Download tarql
print "Downloading Tarql..."
download_file('https://github.com/tarql/tarql/releases/download/v1.1/tarql-1.1-bin.tar.gz', 'tarql.tar.gz')
tar = tarfile.open("tarql.tar.gz")
tar.extractall()
tar.close()
print "Done"

try:
    os.stat('target')
except:
    os.mkdir('target')

counter = 0
# Parsing mapping file
with open('mapping.csv', 'r') as mapping_file:
  mapping_dict = csv.DictReader(mapping_file)
  for line in mapping_dict:
    print 'Elaborating line ' + str(counter) + " ", line
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
      os.system('java -jar jarql.jar ' + line['mapping'] + ' tmp_file >> ' + transform_mapping_name(line['mapping']))
      os.remove('tmp_file')
    else :
      print 'File format not found!!'
      sys.exit(1)
    counter += 1
