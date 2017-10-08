# daf-jsoncsv2rdf-pipeline
Pipeline for tranforming JSON, CSV and all the other separeted values file into RDF.

This project depends on [Tarql](https://github.com/tarql/tarql) and [Jarql](https://github.com/linked-solutions/jarql). The philosophy behind the trasformation is to write a SPARQL construct query in order to map the initial data with your favourite ontology.

## Requirements
* Python 2.7

## How to build
You need to download Tarql and Jarql binary files.
```
python init.py
```

## How to run
Once you have built the project run the pipeline:
```
python run.py
```

The pipeline read `mapping.csv` and for each URL present it downloads the file and converts it in RDF (Turtle) using the mapping file specified. You will find the output files into `target` directory.
