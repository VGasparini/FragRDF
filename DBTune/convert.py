import rdflib
from rdflib import *

g = rdflib.Graph()
g.load('peel.rdf')
print(g.serialize(format='nt'))
