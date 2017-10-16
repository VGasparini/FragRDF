import rdflib																		
import xml.etree.ElementTree as ET
from rdflib import Namespace
import time

def create_part(part,obj):														

	name = "part.t" + str(part+1)
	try:
   		file = open(name, 'r+')
	except:
		file = open(name, 'w+')
	for i in range(len(obj)):
		for j in range(len(obj[i])):
			file.writelines("<"+str(obj[i][j])+">")
			file.writelines('\n')
	file.close()

def file_name(x):													
	return x[(x.rfind("/")+1):]

def reference(g):													
	end = g[(g.rfind("/")+1):]
	ref = Namespace(g[:(g.rfind("/")+1):])
	return ref[end]

def template_read():
	tree = ET.parse('configurefrag.xml')
	root = tree.getroot()

	obj,prop = [],[]
	name,entity,template = [],[],[]
	data = []

	for item in root.iter('item'):
		parent = list(item.attrib.items())
		for i in range(len(parent)):
			obj = parent[i][0]
			prop = parent[i][1]
			if (obj == 'template'):
				template.append(prop)
			elif (obj == 'entity'):
				entity.append(prop)
			elif (obj == 'name'):
				name.append(prop)

	# template	  object 		 predicate
	#  ("T1")	("Product")		("producer")

	template_index = sorted(list(set(template)))

	for i in range(len(template_index)):
		temp2 = []
		for j in range(len(template)):
			temp = []
			if (template_index[i] == template[j]):
				temp.append(entity[j])
				temp.append(name[j])
			if (not not temp): temp2.append(temp)
			del temp
		data.append(temp2)
	del temp2
	
	# Var -> data[template_index[object,predicate]]

	return data,template_index

ini = time.time()

g = rdflib.Graph()
g.parse('teste.nt',format='nt')

schema_ini = time.time()
schema,template_index = template_read()
schema_end = time.time()

data = []

for index in range(len(template_index)):
	objects,predicates = [],[]
	template = template_index[index]

	for instance in range(len(schema[index])):
		objects.append(schema[index][instance][0])
		predicates.append(schema[index][instance][1])
	

	temp = []
	
	for instance in range(len(predicates)):
		
		ref_predicate = reference(predicates[instance])
		type = g.value(ref_predicate)

		temp.append(list(x for x in g.subject_objects(predicate=ref_predicate)))
	
	data.append(temp)

end = time.time()

sort_ini = time.time()
for i in range(len(data)):
	for j in range(len(data[i])):
		data[i][j] = sorted(data[i][j])
sort_end = time.time()

file_ini = time.time()
for i in range(len(data)):
	create_part(i,sorted(data[i]))
file_end = time.time()

print("\n\nTempo de execucao total: {:.3f}s\nTempo verificacao schema: {:.3f}s\nTempo coletar dados: {:.3f}s\nTempo de sort: {:.3f}s\nTempo de criacao dos arquivos: {:.3f}s".format(file_end-ini,schema_end-schema_ini,end-ini,sort_end-sort_ini,file_end-file_ini))
