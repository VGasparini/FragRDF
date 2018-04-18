import rdflib
import xml.etree.ElementTree as ET
from rdflib import Namespace
import time
from pprint import pprint

def create_part(part,name,obj):
	for i in range(len(name)):
		n = str(name[i]) + ".t" + str(part+1)
		try:
	   		file = open(name, 'r+')
		except:
			file = open(name, 'w+')
		for i in range(len(obj)):
			for j in range(len(obj[i])):
				file.writelines(str(obj[i][j])+'\n')
		file.close()

def create_log(log,op):

	name = "log" + str(op) + ".txt"
	try:
   		file = open(name, 'r+')
	except:
		file = open(name, 'w+')
	file.writelines("\n\nTempo de execucao total: {:.3f}s\nTempo verificacao schema: {:.3f}s\nTempo coletar dados: {:.3f}s\nTempo de criacao dos arquivos: {:.3f}s".format(log[0],log[1],log[2],log[3]))
	file.close()

def file_name(data):
	name = []
	for i in range(len(data)):
		for j in range(len(data[i])):
			if (data[i][j][0] == data[i][j][1]):
				name.append(data[i][j][0][(data[i][j][0].rfind("/")+1):])
	return name

def reference(g):
	end = g[(g.rfind("/")+1):]
	ref = Namespace(g[:(g.rfind("/")+1):])
	return ref[end]

def template_reader(path):
	tree = ET.parse(path)
	root = tree.getroot()

	name,entity,template = [],[],[]
	data1,data = [],[[],[],[],[],[],[]]

	for item in root.iter('item'):
		data1.append(list(item.attrib.items()))
	for i in range(len(data1)):
		t = data1[i][1][1] , data1[i][3][1]
		data[int(data1[i][2][1][1:])-1].append(t)
		if(not any(t == data1[i][1][1] for t in name)):
			name.append(data1[i][1][1])
		if(not any(t == data1[i][3][1] for t in entity)):
			entity.append(data1[i][3][1])
		if(not any(t == (int(data1[i][2][1][1:])-1) for t in template)):
			template.append(int(data1[i][2][1][1:])-1)
	# Var -> data[template_index][object,predicate]
	return data,template

base_path = 'dataset.nt'
schema_path = 'configurefrag.xml'

g = rdflib.Graph()
g.parse(base_path,format='nt')

schema,template_index = template_reader(schema_path)

data,name = [],file_name(schema)
temp = []
for index in range(len(template_index)):
	objects,predicates = [],[]

	for instance in range(len(schema[index])):
		objects.append(schema[index][instance][1])
		predicates.append(schema[index][instance][0])

	for instance in range(len(predicates)):
		ref_predicate = reference(predicates[instance])
		ref_object = reference(objects[instance])
		temp.append(list(x for x in g.subject_objects(predicate=ref_predicate)))

	data.append(temp)
	break
pprint(data)

for i in range(len(data)):
	create_part(i,name,sorted(data[i]))
