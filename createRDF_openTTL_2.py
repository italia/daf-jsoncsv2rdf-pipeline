#http://rdflib.readthedocs.io/en/stable/intro_to_parsing.html

from rdflib import Graph

#/home/ubiagio/Documenti/BiagioBlogInformatica/hackathon/20171007_hackDevPA/dev
g = Graph()
#g.parse("../input/csv2rdf_struttura_matera19.ttl", format="nt ttl")
g.parse("../input/csv2rdf_struttura_matera19.ttl", format="turtle")

len(g) # prints 2

import pprint
for stmt in g:
	#g.add((listName, RDF.rest, listItem1))
	#s = g.serialize(format='nt')
    pprint.pprint(stmt)
    
