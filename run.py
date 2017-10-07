import requests
import csv
import tarfile

def download_file(url, filename):
  r = requests.get(url, stream=True)
  with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024): 
      if chunk: # filter out keep-alive new chunks
        f.write(chunk)
  return filename

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

# Parsing mapping file
with open('mapping.csv', 'r') as mapping_file:
  mapping_dict = csv.DictReader(mapping_file)
  for line in mapping_dict:
    print line
