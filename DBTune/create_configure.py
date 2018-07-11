import rdflib
from rdflib import *
from pprint import pprint
import random

g = rdflib.Graph()
g.load('peel.rdf')

name,entity = [],[]

for s,p,o in g.triples((None,RDF.type,None)):
    entity.append(o)
entity = sorted(list(set(entity)))
name = [[] for x in range(len(entity))]

for s,p,o in g.triples((None,RDF.type,None)):
    for i,j,k in g.triples((s,None,None)):
        name[entity.index(o)].append(j)
name = [sorted(list(set(x))) for x in name]

for e in entity:
    for ns in name:
        for n in ns:
            with open('conf.txt', 'a+') as file:
                n = str(n)
                e = str(e)
                file.write(('<item name="{}" entity="{}" pa="PA1" template="T{}"/>\n'.format(n,e,random.randrange(1,7))))
