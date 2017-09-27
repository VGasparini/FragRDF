import xml.etree.ElementTree as ET

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

# template	  entity 		    name
#  ("T1")	("Product")		("producer")

template_index = list(set(template))

for i in range(len(template_index)):
	for j in range(len(template)):
		temp = []
		if (template_index[i] == template[j]):
			temp.append(entitye[j])
			temp.append(name[j])
		data.append(temp)
		del temp
