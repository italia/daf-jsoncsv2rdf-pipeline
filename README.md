# daf-jsoncsv2rdf-pipeline
Pipeline for tranforming CSV data to RDF, developed during [hackdev17](https://hack.developers.italia.it/)

This project depends on [Tarql](https://github.com/tarql/tarql). The idea is to write a SPARQL CONSTRUCT query in order to map the initial [CSV data](http://dati.comune.matera.it/dataset/19luoghidellacultura) with [CULTURAL-ON ontology](http://dati.beniculturali.it/lodview/cis/.html).

# How to build
You need to download Tarql binary files.

# How to run
In bin folder of your Tarql installation, run
```
./tarql 19luoghicultura.sparql 19-luoghi-della-cultura.csv
```

The pipeline read CSV column and for each URL present in the WHERE clause of SPARQL CONSTRUCT query, it converts the value in RDF (Turtle) using a URI for each instance.
