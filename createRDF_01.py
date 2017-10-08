from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, FOAF, OWL, XSD, DC, DCTERMS 
import csv

g = Graph()

cis = Namespace("http://dati.beniculturali.it/cis/")

g.bind("cis", cis)


def create_uri(nome):
    nome="http://www.comune.matera.it/monumenti/"+str(nome.replace(" ","_"))
    return nome


with open('../input/19-luoghi-della-cultura.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    identifier=0;
    
    for row in reader:
        uri_res=create_uri(row['LUOGO'])
        dt = g.resource(uri_res)
        dtg = g.resource(URIRef(str(uri_res)+"_geometry"))
        dta = g.resource(URIRef(str(uri_res)+"_address"))
        dt.add(RDF.type, cis.Site)
        dt.set(cis.hasGeometry, dtg)
        dt.set(cis.hasAddress, dta)
        dtg.add(RDF.type, cis.Geometry)
        dtg.set(cis.hasLatitude,Literal(row['LAT']))
        dtg.set(cis.hasLongitude,Literal(row['LON']))
        dta.add(RDF.type, cis.Address)
        dta.set(cis.fullAddress,Literal(row['INDIRIZZO']))
        
g.serialize(destination='../output/matera19.ttl', format='turtle')
