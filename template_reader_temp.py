import xml.etree.ElementTree as ET

tree = ET.parse('configure_frag.xml')
root = tree.getroot()
obj,prop,name,templ,temp,output = [],[],[],[],[],[]

for item in root.iter('item'):
	parent = list(item.attrib.items())
	for i in range(len(parent)):
		obj = parent[i][0]
		prop = parent[i][1]
		if (obj == 'template'):
			templ.append(prop)
		elif (obj == 'name'):
			name.append(prop)
t = list(set(templ))
for i in range(len(t)):
	for j in range(len(templ)):
		if (t[i] == templ[j]):
			temp.append(name[i])
		output.append(temp)
		del temp[:]
for i in range(len(t)):
	output[i] = sorted(list(set(output[i])))
