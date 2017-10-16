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
