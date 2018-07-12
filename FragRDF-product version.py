# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import rdflib
from rdflib import *
import xml.etree.ElementTree as ET
from pprint import *


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
base_path = "dataset.nt"
schema_path = "configurefrag.xml"

g = rdflib.Graph()
g.load(base_path, format="nt")
template,name,entity = template_reader(schema_path)
for s, p, o in g.triples((None, RDF.type, None)):
    for t in range(len(template)):
        if str(o) in entity[t]:
            for i, j, k in g.triples((s, None, None)):
                if str(j) in name[t]:
                    temp = "<" + str(i) + "> <" + str(j) + "> <" + str(k) + ">\n"
                    write(instance(str(s)),template[t],temp)
