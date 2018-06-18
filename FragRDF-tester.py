import rdflib
from rdflib import *
import xml.etree.ElementTree as ET
from pprint import *
import time
import os

def template_reader(path):
    tree = ET.parse(path)
    root = tree.getroot()
    template = []
    for item in root.iter("items"):
        for items in item.findall("item"):
            if not items.get("template") in template: template.append(items.get("template"))
    entity = [[] for x in range(len(template))]
    name = [[] for x in range(len(template))]
    for item in root.iter("items"):
        for items in item.findall("item"):
    		index = int(items.get("template")[1:])-1
    		entity[index].append(items.get("entity"))
    		name[index].append(items.get("name"))
    return template,name,entity


def instance(obj):
    return obj[obj.rfind('/')+1:]


def write_prod(base,subj,t,obj):
    with open("./files{}/{}.{}".format(base[-8:-3],subj,t), "a+") as file:
        file.write(obj)


def write(base,t,obj):
    with open("/files{}/part.{}".format(base[-8:-3],t), "a+") as file:
        file.write(obj)

base_path = ["dataset01000.nt","dataset02000.nt","dataset05000.nt","dataset10000.nt"]
schema_path = "configurefrag.xml"

g = rdflib.Graph()
for base in base_path:
    os.mkdir("./files{}".format(base[-8:-3]))
    start = time.time()
    g.load(base, format="nt")
    check_1 = time.time()
    template,name,entity = template_reader(schema_path)
    for s, p, o in g.triples((None, RDF.type, None)):
        for t in range(len(template)):
            if str(o) in entity[t]:
                for i, j, k in g.triples((s, None, None)):
                    if str(j) in name[t]:
                        temp = "<" + str(i) + "> <" + str(j) + "> <" + str(k) + ">\n"
                        write_prod(base,instance(str(s)),template[t],temp)
    check_2 = time.time()
    with open("log1-{}.txt".format(base), "a+") as file:
        file.write(("Tempo abertura da base {:.2f}s\nTempo de fragmentacao {:.2f}s\nTempo total {:.2f}s".format(check_1-start,check_2-check_1,check_2-start)))

for base in base_path:
    start = time.time()
    g.load(base, format="nt")
    check_1 = time.time()
    template,name,entity = template_reader(schema_path)
    for s, p, o in g.triples((None, RDF.type, None)):
        for t in range(len(template)):
            if str(o) in entity[t]:
                for i, j, k in g.triples((s, None, None)):
                    if str(j) in name[t]:
                        temp = "<" + str(i) + "> <" + str(j) + "> <" + str(k) + ">\n"
                        write(base,template[t],temp)
    check_2 = time.time()
    with open("log2-{}.txt".format(base), "a+") as file:
        file.write(("Tempo abertura da base {:.2f}s\nTempo de fragmentacao {:.2f}s\nTempo total {:.2f}s".format(check_1-start,check_2-check_1,check_2-start)))
