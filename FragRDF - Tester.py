import rdflib
from rdflib import *
import xml.etree.ElementTree as ET
from pprint import *
import time


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


def write(subj,t,obj):
    with open("{}.{}".format(subj,t), "a+") as file:
        file.write(obj)

start = time.time()
base_path = ["dataset50.nt"]
schema_path = "configurefrag.xml"

g = rdflib.Graph()

for names in range(len(base_path)):
    g.load(base_path[names], format="nt")
    check_1 = time.time()
    template,name,entity = template_reader(schema_path)
    check_2 = time.time()

    for s, p, o in g.triples((None, RDF.type, None)):
        for t in range(len(template)):
            if str(o) in entity[t]:
                for i, j, k in g.triples((s, None, None)):
                    if str(j) in name[t]:
                        temp = "<" + str(i) + "> <" + str(j) + "> <" + str(k) + ">\n"
                        write(instance(str(s)),template[t],temp)

    check_3 = time.time()
    endd = time.time()
    with open("log{}.txt".format(names), "a+") as file:
        file.write(("Tempo abertura da base {:.2f}s\nTempo leitura do configurefrag {:.5f}s\nTempo de fragmentacao {:.2f}s\nTempo total {:.2f}s".format(check_1-start,check_2-check_1,check_3-check_2,endd-start)))
